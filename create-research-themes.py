from pathlib import Path
from html import escape

out = Path(__file__).parent / 'img'
themes = [
    ('Wireless communication', '#285C83', [
        '5G/6G and radio access networks',
        'MIMO and antenna arrays',
        'Cognitive radio and spectrum sharing',
        'Uplink, downlink and relaying',
        'Aerial and backscatter communication']),
    ('Edge computing and IoT', '#28796F', [
        'Internet of Things (IoT)',
        'Mobile edge computing',
        'Sensor networks and sensing',
        'Network slicing and virtualization',
        'Real-time processing and services']),
    ('Artificial intelligence', '#665789', [
        'Machine and deep learning',
        'Reinforcement learning',
        'Neural networks and transformers',
        'Feature extraction and training',
        'Data-driven computational modelling']),
    ('Optimization and resource allocation', '#285C83', [
        'Power and bandwidth allocation',
        'Scheduling and admission control',
        'Energy efficiency and harvesting',
        'Throughput–latency trade-offs',
        'Convex approximation and heuristics']),
    ('Signal processing and inference', '#28796F', [
        'Array signal processing and precoding',
        'Channel estimation and decoding',
        'Interference and noise mitigation',
        'Radar and integrated sensing',
        'Statistical modelling and inference']),
    ('Security and reliability', '#665789', [
        'Communication-system security',
        'Jamming and eavesdropping',
        'Privacy and encryption',
        'Reliable low-latency communication',
        'Robustness under uncertainty']),
]
parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="850" viewBox="0 0 1440 850" role="img" aria-labelledby="title description">
<title id="title">Research themes of the Intelligence, Computing and Communication Lab</title>
<desc id="description">A conceptual taxonomy of keywords from the supplied word cloud, organized into six research themes. All themes have equal visual weight; text size does not represent keyword frequency.</desc>
<style>text{font-family:Arial,Helvetica,sans-serif;fill:#243444}.title{font-size:32px;font-weight:600}.subtitle{font-size:19px;fill:#617080}.heading{font-size:20px;font-weight:600}.term{font-size:18px}.number{font-size:14px;letter-spacing:1.5px;fill:#617080}.note{font-size:15px;fill:#617080}</style>
<rect width="1440" height="850" fill="#fff"/>
<text x="48" y="59" class="title">Research themes</text>
<text x="48" y="92" class="subtitle">Intelligence, Computing &amp; Communication Lab</text>
<path d="M48 116H1392" stroke="#CCD5DC"/>
''']
for i, (title, color, terms) in enumerate(themes):
    x = 48 + (i % 3) * 456
    y = 144 + (i // 3) * 306
    parts.append(f'<g><rect x="{x}" y="{y}" width="432" height="282" rx="5" fill="#FAFBFC" stroke="#DAE0E5"/>')
    parts.append(f'<path d="M{x} {y}H{x+432}" stroke="{color}" stroke-width="4"/>')
    parts.append(f'<text x="{x+22}" y="{y+30}" class="number">THEME {i+1:02}</text>')
    # Keep the long fourth heading on two deliberate lines.
    headings = ['Optimization and', 'resource allocation'] if i == 3 else [title]
    for j, heading in enumerate(headings):
        parts.append(f'<text x="{x+22}" y="{y+59+j*24}" class="heading">{escape(heading)}</text>')
    for j, term in enumerate(terms):
        ty = y + 112 + j * 33
        parts.append(f'<circle cx="{x+25}" cy="{ty-6}" r="2.3" fill="{color}"/>')
        parts.append(f'<text x="{x+38}" y="{ty}" class="term">{escape(term)}</text>')
    parts.append('</g>')
parts.append('''<path d="M48 770H1392" stroke="#CCD5DC"/>
<text x="48" y="802" class="note">Conceptual grouping of the supplied keywords; text size does not encode keyword frequency or research impact.</text>
</svg>''')
(out / 'research-themes.svg').write_text('\n'.join(parts), encoding='utf-8')
print(out / 'research-themes.svg')
