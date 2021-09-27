const commands = document.querySelector('#commands');
const stores = document.querySelector('#stores');

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new window.SpeechRecognition();
recognition.interimResults = true;

recognition.addEventListener('result', (e) =>{
  const text = Array.from(e.results)
  .map(result=>result[0])
  .map(result =>result.transcript)
  .join('');

  if(text.includes('open stores')){
    $("#stores").trigger("click");
  }

  console.log(text);
})
recognition.addEventListener('end',()=>{
  recognition.start();
})

recognition.start();
