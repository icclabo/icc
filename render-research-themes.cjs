const fs = require('fs');
const { chromium } = require('C:/Users/dinhb/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async () => {
  const browser = await chromium.launch({channel:'msedge',headless:true});
  const page = await browser.newPage({viewport:{width:1440,height:850},deviceScaleFactor:2});
  await page.setContent('<style>html,body{margin:0;padding:0}svg{display:block}</style>' + fs.readFileSync('img/research-themes.svg','utf8'));
  const overflow = await page.locator('svg text').evaluateAll(nodes => nodes.filter(n => { const r=n.getBBox(); return r.x+r.width>1400; }).map(n=>n.textContent));
  if(overflow.length) throw Error('Text overflow: '+overflow.join(', '));
  await page.screenshot({path:'img/research-themes.png'});
  await page.pdf({path:'img/research-themes.pdf',width:'1440px',height:'850px',printBackground:true,margin:{top:0,right:0,bottom:0,left:0}});
  await browser.close();
  console.log('Created PNG and PDF. No text exceeds the figure bounds.');
})().catch(error=>{console.error(error);process.exit(1)});
