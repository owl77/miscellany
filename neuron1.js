
  var lock  =0

  var count = 0

  self.addEventListener('message', function(e) {
    console.log(self.name+" excited by " + e.data[0]) 
    count = count + 1
    console.log("neuron1 count " +count)
    if(lock==0){excite()}
    }, false)
    
    
    
  //   if(count < 10){
  //   self.postMessage([self.name,"neuron2"]);}}, false);

  var fastid = setInterval(fire, 3000)

  function fire(){
  self.postMessage([self.name,"neuron2"]) }

  // excitation mechanism

  function reset(){
  console.log("reset")
  clearInterval(slowid)
  fastid= setInterval(fire,3000)
  lock==0  }
  function excite(){
  lock==1
  clearInterval(fastid)
  slowid = setInterval(fire,9000)
  setTimeout(reset,10000) }