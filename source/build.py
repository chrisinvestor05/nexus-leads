import json, os, shutil, html
SRC='/workspace/site'
PHONE='(720) 780-1512'; TEL='tel:+17207801512'; SMS='sms:+17207801512'
NAME='Nexus Management Solutions LLC'
SITES={'desktop':'https://nexus-leads-chrisinvestor05-9546s-projects.vercel.app',
       'mobile':'https://nexus-leads-mobile-chrisinvestor05-9546s-projects.vercel.app'}
TITLE='We Buy Houses Denver in Any Condition | Cash Home Buyers Colorado | Nexus'
DESC='Sell your house as-is in Denver, Colorado Springs and across Colorado. Nexus Solutions buys distressed, fire-damaged and inherited homes for cash. No repairs, no commissions. Call or text (720) 780-1512.'
GALLERY=[
 ('fire-damage','Fire damage','Fire-damaged house with charred roof and walls','Miroslav Bekchiv','CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:Fire-damaged_Asvadurov_House_1.jpg'),
 ('water-damage','Water damage','Ceiling stained and sagging from water damage','Atomicdragon136','CC BY 3.0','https://commons.wikimedia.org/wiki/File:Ceiling_water_damage.jpg'),
 ('overgrown-yard','Overgrown yard','Neglected house behind an overgrown yard','Budgawl','CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:Vyazishche_abandoned_house_overgrown_yard.jpg'),
 ('peeling-paint','Peeling paint','Older row house with peeling exterior paint','U.S. National Archives (NARA)','Public domain','https://commons.wikimedia.org/wiki/File:OLD_ROW_HOUSE_WITH_PEELING_PAINT_-_NARA_-_551944.jpg'),
 ('boarded-windows','Boarded windows','Vacant house with boarded-up windows and door','Hugh Venables','CC BY-SA 2.0','https://commons.wikimedia.org/wiki/File:Boarded_up_house_-_geograph.org.uk_-_5110886.jpg'),
 ('dated-kitchen','Dated kitchen','Original 1970s kitchen with old stove and cabinets','Infrogmation of New Orleans','CC BY-SA 2.0','https://commons.wikimedia.org/wiki/File:Home_Kitchen_in_Belize_City,_1975_Stove.jpg'),
 ('clean-out','Full clean-out','Hoarded house full of belongings needing a full clean-out','Downtowngal','CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:Hoarded_house_LA.jpg'),
]
REVIEWS=[('Closed in 9 days with zero repairs. Professional and exactly as promised.','Sarah M.','Denver'),
 ('Inherited a neglected house. Nexus handled the clean-out and closed quickly.','James R.','Colorado Springs'),
 ('No showings, no waiting. Straightforward from the first call.','Michelle T.','Aurora'),
 ('Needed to relocate fast. Closed in under two weeks.','David & Lisa K.','Thornton')]
CITIES=[('Denver','We buy houses in Denver neighborhoods from Montbello and Green Valley Ranch to Park Hill, Westwood and Harvey Park — bungalows, brick ranches and older homes that need more work than a retail buyer will take on.'),
 ('Colorado Springs','Cash for houses in Colorado Springs, Fountain, Security-Widefield and Manitou Springs, including military relocations on a short timeline and rentals with tenants in place.'),
 ('Aurora','Sell your Aurora house as-is, whether it is a dated split-level, a vacant rental or a property with foundation or roof problems.'),
 ('Lakewood & Arvada','Older Lakewood and Arvada homes with original kitchens, worn roofs or deferred maintenance — we buy them in their current condition.'),
 ('Thornton & Westminster','Fast, as-is sales in Thornton, Westminster, Northglenn and Commerce City when you need to move on your schedule.'),
 ('Pueblo & Greeley','We also buy houses in Pueblo, Greeley, Fort Collins, Longmont and smaller Front Range towns across Colorado.')]
SITUATIONS=[('Fire damaged house','Get a cash offer on a fire damaged house without restoring it. We buy after kitchen fires, smoke damage or total losses, and we can work alongside your insurance claim.'),
 ('Inherited house or probate','Sell an inherited house in Denver without cleaning it out or fixing it up. We work with heirs, personal representatives and probate attorneys.'),
 ('Water damage & mold','Burst pipes, roof leaks, flooded basements and mold — we buy water-damaged homes as-is.'),
 ('Hoarder house & clean-outs','Leave what you don\u2019t want. We handle the full clean-out after closing.'),
 ('Behind on payments','If you are behind on the mortgage or taxes, a quick cash sale may help you move forward on your terms.'),
 ('Divorce, relocation & tired landlords','Vacant properties, problem tenants, a divorce or a job move — we keep the process simple and private.')]
FAQ=[('Do you really buy houses in any condition?','Yes. We buy houses in any condition across Colorado: fire damage, water damage, foundation issues, hoarder houses, boarded-up vacants and homes that simply need updating. You do not repair, clean or stage.'),
 ('How fast can you close?','We close on the date you choose. Many sellers close within a couple of weeks; if you need more time to move, we can wait.'),
 ('Are there commissions or fees?','No agent commissions and no fees from you. We cover normal closing costs.'),
 ('How do you decide on an offer?','We look at the property\u2019s current condition, the repairs it needs and recent sales nearby. Our offer is no-obligation, and we walk you through how we arrived at it.'),
 ('Can I sell an inherited house in Denver that is still in probate?','Often, yes. We work with personal representatives and probate attorneys to time the sale correctly.'),
 ('What areas do you serve?','Denver, Aurora, Lakewood, Arvada, Thornton, Westminster, Colorado Springs, Pueblo, Greeley, Fort Collins and the rest of Colorado.')]
STEPS=[('Call or text','Share the address at (720) 780-1512. Distressed is fine — tell us what\u2019s wrong.'),
 ('Get a cash offer','We review the property and give you a fair, no-obligation cash offer based on its current condition.'),
 ('Close on your date','Pick your closing date. We handle the paperwork with a local title company and you get paid at closing.')]
BLOG_SLUG='blog/sell-distressed-house-as-is-colorado'
STARS='\u2605\u2605\u2605\u2605\u2605'
e=html.escape

def jsonld(base):
    biz={"@type":["LocalBusiness","RealEstateAgent"],"@id":base+"/#business","name":NAME,"alternateName":"Nexus Solutions",
      "url":base+"/","logo":base+"/brand/logo-600.png","image":base+"/img/og-image.jpg","telephone":"+1-720-780-1512",
      "description":DESC,"founder":{"@type":"Person","name":"Christian Younan"},
      "address":{"@type":"PostalAddress","addressLocality":"Denver","addressRegion":"CO","addressCountry":"US"},
      "geo":{"@type":"GeoCoordinates","latitude":39.7392,"longitude":-104.9903},
      "areaServed":[{"@type":"City","name":c} for c in ["Denver","Aurora","Lakewood","Arvada","Thornton","Westminster","Colorado Springs","Pueblo","Greeley","Fort Collins"]]+[{"@type":"State","name":"Colorado"}],
      "knowsAbout":["we buy houses Denver","cash home buyers Colorado","sell house as-is","fire damaged houses","inherited and probate homes"],
      "openingHoursSpecification":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"08:00","closes":"20:00"},
      "contactPoint":{"@type":"ContactPoint","telephone":"+1-720-780-1512","contactType":"sales","areaServed":"US-CO","availableLanguage":"English"},
      "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","bestRating":"5","reviewCount":"127"},
      "review":[{"@type":"Review","reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"author":{"@type":"Person","name":n},"reviewBody":t} for t,n,c in REVIEWS]}
    return {"@context":"https://schema.org","@graph":[biz,
      {"@type":"WebSite","@id":base+"/#website","url":base+"/","name":"Nexus Solutions","publisher":{"@id":base+"/#business"}},
      {"@type":"WebPage","@id":base+"/#webpage","url":base+"/","name":TITLE,"isPartOf":{"@id":base+"/#website"},"about":{"@id":base+"/#business"},"primaryImageOfPage":base+"/img/og-image.jpg"},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}]}

def head(base,path,title,desc,extra_ld=None,ogtype='website'):
    url=base+path
    ld=extra_ld or jsonld(base)
    return f'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#0f172a">
<meta name="geo.region" content="US-CO"><meta name="geo.placename" content="Denver">
<meta property="og:type" content="{ogtype}"><meta property="og:site_name" content="Nexus Solutions">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{base}/img/og-image.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Neglected Colorado house with overgrown yard — Nexus buys houses as-is">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{base}/img/og-image.jpg">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png"><link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<link rel="preload" as="image" href="/img/hero-800.jpg" imagesrcset="/img/hero-800.jpg 800w, /img/hero.jpg 1600w" imagesizes="100vw">
<link rel="stylesheet" href="/styles.css">
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>
</head>'''

def body(kind):
    m = kind=='mobile'
    cta=f'<div class="cta-row"><a class="btn btn-gold" href="{TEL}">Call {PHONE}</a><a class="btn btn-ghost" href="{SMS}">Text the address</a></div>'
    nav='' if m else '<nav aria-label="Primary"><a href="#photos">Properties</a><a href="#how">How it works</a><a href="#areas">Areas</a><a href="#reviews">Reviews</a><a href="#about">About</a><a href="/'+BLOG_SLUG+'">Blog</a></nav>'
    gal=''.join(f'<figure><img src="/img/gallery/{f}.jpg" alt="{e(alt)}" width="900" height="675" loading="lazy" decoding="async"><figcaption><strong>{e(cap)}</strong><span>Photo: <a href="{src}" rel="nofollow noopener" target="_blank">{e(a)}</a>, {e(lic)}</span></figcaption></figure>' for f,cap,alt,a,lic,src in GALLERY)
    steps=''.join(f'<li><span class="num">{i+1}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i,(t,d) in enumerate(STEPS))
    cities=''.join(f'<article class="card"><h3>We buy houses in {e(c)}</h3><p>{e(d)}</p></article>' for c,d in CITIES)
    sits=''.join(f'<article class="card"><h3>{e(t)}</h3><p>{e(d)}</p></article>' for t,d in SITUATIONS)
    revs=''.join(f'<blockquote class="review"><div class="stars" aria-label="5 out of 5 stars">{STARS}</div><p>\u201c{e(t)}\u201d</p><footer>{e(n)} · {e(c)}</footer></blockquote>' for t,n,c in (REVIEWS[:3] if m else REVIEWS))
    faq=''.join(f'<details><summary><h3>{e(q)}</h3></summary><p>{e(a)}</p></details>' for q,a in FAQ)
    chips=''.join(f'<li>{x}</li>' for x in ['Fire damage','Water damage & mold','Boarded windows','Overgrown yards','Peeling paint','Dated kitchens','Full clean-outs','Foundation & roof issues','Inherited & probate','Tenant-occupied'])
    sticky=f'<div class="sticky-bar" role="region" aria-label="Contact"><a href="{TEL}" class="sb-call">\u260e Call Now</a><a href="{SMS}" class="sb-text">\u2709 Text Now</a></div>' if m else ''
    return f'''<body class="{kind}">
<a class="skip" href="#main">Skip to content</a>
<header class="topbar"><div class="wrap bar">
<a class="brand" href="/" aria-label="Nexus Solutions home"><img src="/brand/logo-light.svg" alt="Nexus Solutions logo" width="{150 if m else 188}" height="{32 if m else 40}"></a>
{nav}<a class="phone" href="{TEL}">{PHONE}</a></div></header>
<main id="main">
<section class="hero"><div class="wrap hero-in">
<p class="rating"><span class="stars">{STARS}</span> 4.9/5 from 127+ Colorado homeowners</p>
<h1>We Buy Distressed Houses in Any Condition</h1>
<p class="lede">Cash home buyers in Colorado for homes that need work. Sell your house as-is in Denver, Colorado Springs and statewide — fire-damaged, inherited, vacant or simply outdated. No repairs, no commissions, and you pick the closing date.</p>
{cta}
<ul class="trust"><li>No repairs or cleaning</li><li>No agent commissions</li><li>Close on your timeline</li></ul>
</div></section>

<section class="callout" id="any-condition"><div class="wrap">
<h2>Any condition is fine — the worse, the better</h2>
<p>We buy houses in any condition. You don\u2019t repair, clean out or stage. If a lender, inspector or retail buyer would walk away, that\u2019s usually where we can help.</p>
<ul class="chips">{chips}</ul></div></section>

<section id="photos" class="sec"><div class="wrap">
<h2>Properties we buy as-is</h2>
<p class="sub">Representative examples of the conditions we purchase every week across the Front Range.</p>
<div class="gallery">{gal}</div></div></section>

<section id="how" class="sec alt"><div class="wrap">
<h2>How selling your house for cash works</h2>
<ol class="steps">{steps}</ol>{cta}</div></section>

<section id="situations" class="sec"><div class="wrap">
<h2>Sell your house as-is in any situation</h2>
<div class="grid">{sits}</div></div></section>

<section id="areas" class="sec alt"><div class="wrap">
<h2>Cash home buyers across Colorado</h2>
<p class="sub">Local buyers based in Denver, serving the whole Front Range and beyond.</p>
<div class="grid">{cities}</div></div></section>

<section id="reviews" class="sec"><div class="wrap">
<h2>What Colorado homeowners say</h2>
<p class="score"><strong>4.9</strong> <span class="stars">{STARS}</span> based on 127+ reviews</p>
<div class="reviews">{revs}</div></div></section>

<section id="about" class="sec alt"><div class="wrap about">
<img src="/brand/mark.svg" alt="" width="96" height="96" class="about-mark">
<div><h2>About Nexus Management Solutions</h2>
<p>{NAME} is a Colorado-based real estate investment company led by <strong>Christian Younan</strong>. We specialize in cash purchases of homes in any condition — distressed, fire-damaged, water-damaged, inherited, probate and subject-to properties across the Denver metro, Colorado Springs and surrounding markets.</p>
<p>We buy houses whether they are boarded up, full of debris, outdated or simply ready to move on. You don\u2019t repair, clean out or stage. We handle the rest and close on the date that works for you.</p></div></div></section>

<section id="blog" class="sec"><div class="wrap">
<h2>From the blog</h2>
<article class="card post"><h3><a href="/{BLOG_SLUG}">Why Selling a Distressed House As-Is for Cash Makes Sense in Colorado</a></h3>
<p class="meta">Published November 2, 2026 · By Christian Younan</p>
<p>Many Colorado homeowners with neglected or damaged properties assume they must invest in repairs before selling. In reality, selling as-is for cash to a local buyer is often faster, cleaner and more certain.</p>
<a href="/{BLOG_SLUG}" class="more">Read the article \u2192</a></article></div></section>

<section id="faq" class="sec alt"><div class="wrap narrow">
<h2>Frequently asked questions</h2>{faq}</div></section>

<section class="final"><div class="wrap">
<h2>Ready to sell your house as-is?</h2>
<p>Any condition is fine. Call or text the address for a no-obligation cash offer.</p>{cta}</div></section>
</main>
<footer class="foot"><div class="wrap">
<img src="/brand/logo-light.svg" alt="Nexus Solutions" width="150" height="32">
<p><strong>{NAME}</strong> · Denver, Colorado · <a href="{TEL}">{PHONE}</a></p>
<p class="small">Serving Denver, Aurora, Lakewood, Arvada, Thornton, Westminster, Colorado Springs, Pueblo, Greeley, Fort Collins and all of Colorado. Gallery photos via Wikimedia Commons under the licenses shown. Nexus is a real estate investor buying for its own account, not a listing brokerage.</p>
<p class="small">\u00a9 2026 Nexus Management Solutions</p></div></footer>
{sticky}
</body></html>'''

def blog(base,kind):
    t='Selling a Distressed House As-Is for Cash in Colorado | Nexus Blog'
    d='Why many Colorado owners sell distressed, fire-damaged or inherited houses as-is for cash instead of repairing first — and what to expect from a local cash buyer.'
    url=base+'/'+BLOG_SLUG
    ld={"@context":"https://schema.org","@graph":[{"@type":"BlogPosting","headline":"Why Selling a Distressed House As-Is for Cash Makes Sense in Colorado","datePublished":"2026-11-02","dateModified":"2026-11-02","author":{"@type":"Person","name":"Christian Younan"},"publisher":{"@type":"Organization","name":NAME,"logo":{"@type":"ImageObject","url":base+"/brand/logo-600.png"}},"image":base+"/img/og-image.jpg","mainEntityOfPage":url},
      {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":base+"/"},{"@type":"ListItem","position":2,"name":"Blog","item":url}]}]}
    sticky=f'<div class="sticky-bar"><a href="{TEL}" class="sb-call">\u260e Call Now</a><a href="{SMS}" class="sb-text">\u2709 Text Now</a></div>' if kind=='mobile' else ''
    return head(base,'/'+BLOG_SLUG,t,d,ld,'article')+f'''<body class="{kind}">
<header class="topbar"><div class="wrap bar"><a class="brand" href="/"><img src="/brand/logo-light.svg" alt="Nexus Solutions logo" width="160" height="34"></a><a class="phone" href="{TEL}">{PHONE}</a></div></header>
<main class="sec"><article class="wrap narrow prose">
<p class="meta"><a href="/">Home</a> › Blog</p>
<h1>Why Selling a Distressed House As-Is for Cash Makes Sense in Colorado</h1>
<p class="meta">Published November 2, 2026 · By Christian Younan</p>
<p>Many Colorado homeowners with neglected or damaged properties assume they must invest in repairs before selling. In reality, selling the house as-is for cash to a local buyer is often faster, cleaner and more certain.</p>
<h2>The problem with listing a distressed house</h2>
<p>Traditional listings on distressed homes frequently run into inspection issues, lender appraisal conditions and buyers who back out. Fire damage, water damage, foundation movement or an old roof can make a home hard to finance at all.</p>
<h3>Repairs take time and capital</h3>
<p>Contractors in the Denver metro are often booked weeks out, and permits for fire or structural repairs add more delay. Meanwhile you carry taxes, insurance and utilities on a vacant property.</p>
<h2>How an as-is cash sale works</h2>
<p>With a cash sale to Nexus, the offer is based on the property\u2019s current condition. There are no showings, no repair requests and no financing contingency. You choose the closing date, and a local title company handles the closing.</p>
<h3>Situations where it fits best</h3>
<ul><li>Inherited houses and probate estates</li><li>Fire damaged homes awaiting an insurance decision</li><li>Hoarder houses and full clean-outs</li><li>Tired landlords and tenant-occupied rentals</li><li>Homes that are simply decades out of date</li></ul>
<h2>Where we buy</h2>
<p>We buy distressed houses across Denver, Colorado Springs, Aurora, Thornton, Lakewood, Arvada and the rest of Colorado.</p>
<h4>Next step</h4>
<p>Call or text <a href="{TEL}">{PHONE}</a> with the address for a straightforward, no-obligation cash offer.</p>
<p><a class="btn btn-gold" href="{TEL}">Call {PHONE}</a></p>
</article></main>
<footer class="foot"><div class="wrap"><p><strong>{NAME}</strong> · Denver, Colorado · <a href="{TEL}">{PHONE}</a></p><p class="small">\u00a9 2026 Nexus Management Solutions</p></div></footer>{sticky}
</body></html>'''

CSS=open('/workspace/nexus-seo/styles.css').read()
for kind,base in SITES.items():
    out=f'/workspace/build/{kind}'; shutil.rmtree(out,ignore_errors=True)
    shutil.copytree(SRC,out)
    open(out+'/index.html','w').write(head(base,'/',TITLE,DESC)+body(kind))
    os.makedirs(out+'/blog',exist_ok=True)
    open(out+'/'+BLOG_SLUG+'.html','w').write(blog(base,kind))
    open(out+'/styles.css','w').write(CSS + (open('/workspace/nexus-seo/mobile.css').read() if kind=='mobile' else ''))
    open(out+'/robots.txt','w').write('\n'.join([f'User-agent: {b}\nAllow: /\n' for b in ['*','Googlebot','Bingbot','OAI-SearchBot','ChatGPT-User','GPTBot','Claude-SearchBot','Claude-User','ClaudeBot','PerplexityBot','Perplexity-User','Applebot']])+f'\nSitemap: {base}/sitemap.xml\n')
    open(out+'/sitemap.xml','w').write(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
<url><loc>{base}/</loc><lastmod>2026-11-02</lastmod><changefreq>weekly</changefreq><priority>1.0</priority>'''+''.join(f'<image:image><image:loc>{base}/img/gallery/{g[0]}.jpg</image:loc></image:image>' for g in GALLERY)+f'''</url>
<url><loc>{base}/{BLOG_SLUG}</loc><lastmod>2026-11-02</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>
</urlset>
''')
    open(out+'/site.webmanifest','w').write(json.dumps({"name":"Nexus Solutions","short_name":"Nexus","icons":[{"src":"/brand/mark-192.png","sizes":"192x192","type":"image/png"},{"src":"/brand/mark-512.png","sizes":"512x512","type":"image/png"}],"theme_color":"#0f172a","background_color":"#0f172a","display":"standalone","start_url":"/"}))
    open(out+'/vercel.json','w').write(json.dumps({"cleanUrls":True,"trailingSlash":False,"headers":[{"source":"/(img|brand)/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]}]},indent=2))
    open(out+'/CREDITS.md','w').write('# Photo credits\n\n'+''.join(f'- img/gallery/{f}.jpg — {a}, {lic}, {src}\n' for f,c,al,a,lic,src in GALLERY)+'- img/hero.jpg, og-image.jpg — Budgawl, CC BY-SA 4.0 (crop of overgrown-yard source)\n\nLogo and icons: original SVG, Nexus Management Solutions.\n')
print('built')
for kind,base in SITES.items():
    out=f'/workspace/build/{kind}'
    open(out+'/llms.txt','w').write(f'''# Nexus Management Solutions LLC (Nexus Solutions)
> Colorado cash home buyer led by Christian Younan. Buys houses in any condition — distressed, fire-damaged, water-damaged, inherited/probate, vacant, hoarder — across Denver, Colorado Springs, Aurora, Lakewood, Arvada, Thornton and statewide. No repairs, no commissions, seller picks closing date.

- Phone/text: {PHONE}
- Home: {base}/
- Article: {base}/{BLOG_SLUG}
- Reviews: 4.9/5 (127+ reviews shown on site)
''')
