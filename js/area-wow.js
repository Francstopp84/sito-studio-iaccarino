/* AREE E PAGINE REATO: barra, comparsa, luce cursore, pulsante consulenza */
(function(){var d=document,rm=matchMedia('(prefers-reduced-motion:reduce)').matches;d.documentElement.classList.add('js');
var pb=d.createElement('div');pb.className='progress';d.body.appendChild(pb);
addEventListener('scroll',function(){var h=d.documentElement;pb.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%'},{passive:true});
var els=d.querySelectorAll('.norma-box,.fascia,.strategia,.caso-detail,.area-card,.competenza,.step,.section-title');
els.forEach(function(e){e.classList.add('rv2')});
if('IntersectionObserver' in window&&!rm){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.1});els.forEach(function(e){io.observe(e)})}else{els.forEach(function(e){e.classList.add('in')})}
d.addEventListener('pointermove',function(e){var c=e.target.closest&&e.target.closest('.norma-box,.fascia,.strategia,.caso-detail,.area-card,.competenza');if(!c)return;var r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px')});
var cta=d.querySelector('.nav-cta-link');if(cta){var f=d.createElement('a');f.className='fab-consulenza';f.href=cta.getAttribute('href');f.textContent='Richiedi la consulenza';d.body.appendChild(f)}
})();
