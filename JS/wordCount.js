document.addEventListener("DOMContentLoaded", function() {
    var message = document.getElementById("message");
    var wordCountElement = document.getElementById("word-count");
  
    function updateCharacterCount() {
      var remainingCharacters = 5000 - message.value.length;
      wordCountElement.innerText = Math.max(remainingCharacters, 0) + " characters remaining";
  
      if (remainingCharacters < 0) {
        message.value = message.value.substring(0, 5000);
        wordCountElement.style.color = "red";
      } else {
        wordCountElement.style.color = "gray";
      }
    }
  
    message.addEventListener("input", updateCharacterCount);
  });