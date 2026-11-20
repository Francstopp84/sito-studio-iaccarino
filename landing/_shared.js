// Tracking conversioni via GTM/dataLayer + Form handler Netlify Forms
window.dataLayer = window.dataLayer || [];

document.addEventListener("click", function(e){
  const a = e.target.closest("a");
  if(!a) return;
  const href = a.getAttribute("href") || "";
  const area = document.body.dataset.area || "unknown";
  if(href.startsWith("tel:")){
    window.dataLayer.push({event: "click_telefono", area: area, value: 50, currency: "EUR"});
  } else if(href.includes("wa.me")){
    window.dataLayer.push({event: "click_whatsapp", area: area, value: 30, currency: "EUR"});
  }
});

// Form: usa Netlify Forms nativo (submit standard), intercetta solo per tracking
(function(){
  const form = document.querySelector("form.lead-form");
  if(!form) return;
  form.addEventListener("submit", function(){
    const area = document.body.dataset.area || "unknown";
    window.dataLayer.push({event: "submit_form", area: area, value: 50, currency: "EUR"});
  });
})();
