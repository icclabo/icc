const fs=require('fs');
const {chromium}=require('C:/Users/dinhb/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
const browser=await chromium.launch({channel:'msedge',headless:true});
const page=await browser.newPage();
const png='data:image/png;base64,'+fs.readFileSync('img/wordcloud-refined.png').toString('base64');
const compressed=await page.evaluate(async src=>{const image=new Image();image.src=src;await image.decode();const canvas=document.createElement('canvas');canvas.width=image.naturalWidth;canvas.height=image.naturalHeight;canvas.getContext('2d').drawImage(image,0,0);return {url:canvas.toDataURL('image/webp',.93),width:image.naturalWidth,height:image.naturalHeight};},png);
const fragment=fs.readFileSync('wordcloud-animation.fragment.html','utf8').replace('__CLOUD_IMAGE__',compressed.url);
const dir='C:/Users/dinhb/.codex/visualizations/2026/09/22/01a0c992-e874-7390-b964-48fcf3ebc8a3/';
fs.writeFileSync(dir+'animated-wordcloud.html',fragment);
fs.writeFileSync('wordcloud-animated.html','<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ICC Lab animated word cloud</title><style>html,body{margin:0;background:#fff}</style></head><body>'+fragment+'</body></html>');
await page.setViewportSize({width:900,height:700});await page.setContent(fragment);
await page.waitForTimeout(1100);await page.screenshot({path:dir+'wordcloud-animation-preview.png'});
const first=await page.locator('.focus-word').getAttribute('data-keyword');
await page.waitForTimeout(1900);const second=await page.locator('.focus-word').getAttribute('data-keyword');
console.log(JSON.stringify({width:compressed.width,height:compressed.height,bytes:Buffer.byteLength(fragment),first,second,activeAnimations:await page.evaluate(()=>document.getAnimations().filter(a=>a.playState==='running').length)}));
await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
