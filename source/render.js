const {Resvg}=require('@resvg/resvg-js');const fs=require('fs');const b='/workspace/site/brand/';
const r=(src,w,out,bg)=>{const png=new Resvg(fs.readFileSync(b+src,'utf8'),{fitTo:{mode:'width',value:w},background:bg,font:{loadSystemFonts:true}}).render().asPng();fs.writeFileSync(out,png);};
for(const s of [16,32,48,180,192,512]) r('mark.svg',s,b+`mark-${s}.png`);
for(const w of [300,600,1200]) r('logo.svg',w,b+`logo-${w}.png`);
for(const w of [600,1200]) r('logo-light.svg',w,b+`logo-light-${w}.png`);
fs.copyFileSync(b+'mark-180.png','/workspace/site/apple-touch-icon.png');
fs.copyFileSync(b+'mark-32.png','/workspace/site/favicon-32x32.png');
fs.copyFileSync(b+'mark-16.png','/workspace/site/favicon-16x16.png');
fs.copyFileSync(b+'mark.svg','/workspace/site/favicon.svg');
