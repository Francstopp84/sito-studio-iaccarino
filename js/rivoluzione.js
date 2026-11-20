/* RIVOLUZIONE 20.11.2026 */
(function(){
document.documentElement.classList.add('js');
var nav=document.querySelector('.nav'),bg=document.querySelector('.burger'),ln=document.querySelector('.links');
function sc(){nav&&nav.classList.toggle('s',window.scrollY>30)}sc();window.addEventListener('scroll',sc,{passive:true});
if(bg&&ln){bg.addEventListener('click',function(){var o=ln.classList.toggle('o');bg.setAttribute('aria-expanded',o)});
ln.addEventListener('click',function(e){if(e.target.tagName==='A'){ln.classList.remove('o');bg.setAttribute('aria-expanded','false')}})}
/* reveal una volta sola */
var els=document.querySelectorAll('.rv');
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});els.forEach(function(e){io.observe(e)})}else{els.forEach(function(e){e.classList.add('in')})}
/* filtri casi: area + ricerca + mostra altri */
(function(){var gr=document.querySelector('.griglia-casi[data-lim]');if(!gr)return;
var cs=[].slice.call(gr.querySelectorAll('.caso')),lim=+gr.getAttribute('data-lim'),sh=lim,area='tutti',q='';
var bt=document.querySelectorAll('.filtri button'),inp=document.getElementById('cerca'),al=document.getElementById('altri'),ct=document.getElementById('conta');
cs.forEach(function(c){c.setAttribute('data-t',(c.textContent||'').toLowerCase())});
function ag(){var n=0,v=0;cs.forEach(function(c){var ok=(area==='tutti'||c.getAttribute('data-area')===area)&&(!q||c.getAttribute('data-t').indexOf(q)>-1);if(ok){n++;c.hidden=v>=sh;if(!c.hidden)v++}else c.hidden=true});
if(ct)ct.textContent=n+(n===1?' caso trovato':' casi trovati');if(al)al.style.display=n>sh?'':'none'}
[].forEach.call(bt,function(b){b.addEventListener('click',function(){[].forEach.call(bt,function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});area=b.getAttribute('data-f');sh=lim;ag()})});
if(inp)inp.addEventListener('input',function(){q=inp.value.trim().toLowerCase();sh=lim;ag()});
if(al)al.addEventListener('click',function(){sh+=24;ag()});
cs.forEach(function(c){if(c.textContent.length>700){c.classList.add('lungo');var bb=document.createElement('button');bb.type='button';bb.className='leggi';bb.textContent='Leggi tutto';bb.addEventListener('click',function(){var o=c.classList.toggle('aperto');bb.textContent=o?'Chiudi':'Leggi tutto'});c.appendChild(bb)}});
var h=(location.hash||'').slice(1);if(h){[].forEach.call(bt,function(b){if(b.getAttribute('data-f')===h)b.click()})}
ag()})();
/* filtri home (vetrina) */
document.querySelectorAll('.filtri').forEach(function(f){var gr=f.parentNode.querySelector('.griglia-casi');if(!gr||gr.hasAttribute('data-lim'))return;
f.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;f.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});var a=b.getAttribute('data-f');gr.querySelectorAll('.caso').forEach(function(c){c.hidden=!(a==='tutti'||c.getAttribute('data-area')===a)})})});
/* cookie */
var ck=document.querySelector('.cookie');
if(ck){try{if(!localStorage.getItem('ck_ok'))ck.classList.add('v')}catch(e){ck.classList.add('v')}
ck.querySelector('button').addEventListener('click',function(){try{localStorage.setItem('ck_ok','1')}catch(e){}ck.classList.remove('v')})}
/* form */
var fm=document.getElementById('form-contatti');
if(fm){fm.addEventListener('submit',function(e){e.preventDefault();var b=fm.querySelector('button[type=submit]');b.disabled=true;b.textContent='Invio in corso';
var d=new FormData(fm);
fetch(fm.action,{method:'POST',body:d,headers:{'Accept':'application/json'}}).then(function(r){return r.json()}).then(function(){window.location.href='grazie.html'}).catch(function(){b.disabled=false;b.textContent='Richiedi il colloquio';alert('Invio non riuscito: scriva a studiolegalefrancescoiaccarino@outlook.com o chiami il 333 568 4659.')})})}
/* scena 3D: solo desktop, no reduced-motion, sospesa fuori vista */
var cv=document.getElementById('scena');
if(!cv||window.matchMedia('(prefers-reduced-motion:reduce)').matches||window.innerWidth<900)return;
import('https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js').then(function(T){
var r=new T.WebGLRenderer({canvas:cv,alpha:true,antialias:true});r.setPixelRatio(Math.min(devicePixelRatio,1.6));
var s=new T.Scene(),c=new T.PerspectiveCamera(45,1,.1,100);c.position.set(0,0,9);
var g=new T.Group();s.add(g);
var m1=new T.MeshBasicMaterial({color:0xd8b46a,wireframe:true,transparent:true,opacity:.55});
var ico=new T.Mesh(new T.IcosahedronGeometry(2.3,1),m1);g.add(ico);
var ico2=new T.Mesh(new T.OctahedronGeometry(3.4,0),new T.MeshBasicMaterial({color:0x4a78b8,wireframe:true,transparent:true,opacity:.28}));g.add(ico2);
var n=900,p=new Float32Array(n*3);for(var i=0;i<n;i++){var a=Math.random()*6.283,b=Math.acos(2*Math.random()-1),R=4+Math.random()*5;p[i*3]=R*Math.sin(b)*Math.cos(a);p[i*3+1]=R*Math.sin(b)*Math.sin(a);p[i*3+2]=R*Math.cos(b)}
var pg=new T.BufferGeometry();pg.setAttribute('position',new T.BufferAttribute(p,3));
var pts=new T.Points(pg,new T.PointsMaterial({color:0xf1d89a,size:.035,transparent:true,opacity:.8}));s.add(pts);
g.position.x=3.2;
function rs(){var w=cv.clientWidth,h=cv.clientHeight;r.setSize(w,h,false);c.aspect=w/h;c.updateProjectionMatrix()}rs();window.addEventListener('resize',rs);
var vis=true,sy=0;new IntersectionObserver(function(e){vis=e[0].isIntersecting}).observe(cv);
window.addEventListener('scroll',function(){sy=window.scrollY},{passive:true});
var t0=performance.now();
(function loop(){requestAnimationFrame(loop);if(!vis)return;var t=(performance.now()-t0)/1000;
ico.rotation.y=t*.12+sy*.0012;ico.rotation.x=sy*.0008+.3;ico2.rotation.y=-t*.07-sy*.001;ico2.rotation.z=t*.05;
pts.rotation.y=t*.02+sy*.0004;g.position.y=-sy*.002;r.render(s,c)})()}).catch(function(){})
})();

/* WOW 2026: barra, contatori, luce sul cursore, tilt */
(function(){var rm=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
var pb=document.createElement('div');pb.className='progress';document.body.appendChild(pb);
window.addEventListener('scroll',function(){var h=document.documentElement;pb.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%'},{passive:true});
function cnt(el){var n=parseInt(el.textContent,10);if(!n||rm)return;var d=1400,t0=performance.now();el.textContent='0';(function f(t){var p=Math.min((t-t0)/d,1);el.textContent=Math.round(n*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)})(t0)}
var cs=document.querySelectorAll('.bignum,.tile b,.kpi b');
if('IntersectionObserver' in window){var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){cnt(e.target);o.unobserve(e.target)}})},{threshold:.5});cs.forEach(function(e){if(/^\d+$/.test(e.textContent.trim()))o.observe(e)})}
document.addEventListener('pointermove',function(e){var c=e.target.closest&&e.target.closest('.tile,.area,.caso,.guida');if(!c)return;var r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px');
if(!rm&&c.classList.contains('area')&&e.pointerType==='mouse'){var x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform='perspective(800px) rotateY('+(x*8)+'deg) rotateX('+(-y*8)+'deg) translateY(-4px)'}});
document.addEventListener('pointerout',function(e){var c=e.target.closest&&e.target.closest('.area');if(c)c.style.transform=''});
})();

/* AIUTO NAPOLI */
(function(){
var f=document.querySelector('.ai-f');
if(f){var ds=document.querySelectorAll('details.ai');
f.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;f.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});var a=b.getAttribute('data-f');ds.forEach(function(d){d.hidden=!(a==='tutti'||d.getAttribute('data-area')===a);if(d.hidden)d.open=false})});
ds.forEach(function(d){d.addEventListener('toggle',function(){if(d.open)ds.forEach(function(o){if(o!==d)o.open=false})})})}
var nf=document.getElementById('nf'),np=document.getElementById('npan');
if(nf&&np){var hs=nf.querySelectorAll('.hs'),hp=np.querySelectorAll('.hp'),h0=np.querySelector('.hp0');
function show(i){hs.forEach(function(b){b.classList.toggle('on',b.getAttribute('data-i')==i)});hp.forEach(function(p){p.hidden=p.getAttribute('data-i')!=i});h0.hidden=true}
hs.forEach(function(b){b.addEventListener('click',function(){show(b.getAttribute('data-i'))});b.addEventListener('mouseenter',function(){if(matchMedia('(hover:hover)').matches)show(b.getAttribute('data-i'))})});
var im=nf.querySelector('img'),rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
if(!rm){nf.addEventListener('pointermove',function(e){if(e.pointerType!=='mouse')return;var r=nf.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;im.style.transform='scale(1.12) translate('+(-x*18)+'px,'+(-y*12)+'px)'});
nf.addEventListener('pointerleave',function(){im.style.transform=''});
window.addEventListener('scroll',function(){var r=nf.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;var p=(r.top+r.height/2-innerHeight/2)/innerHeight;if(!nf.matches(':hover'))im.style.transform='scale(1.12) translateY('+(p*-20)+'px)'},{passive:true})}}
})();
