

  var count = 0
  self.addEventListener('message', function(e) {
    count = count + 1
    console.log(self.name+" excited by " + e.data[0]) 
     self.postMessage([self.name,"neuron1"]);
     console.log("neuron2 count " + count)
  }, false);