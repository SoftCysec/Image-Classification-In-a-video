/* static/js/script.js */

document.addEventListener('DOMContentLoaded', function() {
    // Add an event listener to the submit button
    document.querySelector('form').addEventListener('submit', function(event) {
      // Prevent the form from being submitted
      event.preventDefault();
  
      // Get the file input element
      var fileInput = document.querySelector('input[type="file"]');
  
      // Check if a file has been selected
      if (fileInput.files.length > 0) {
        // Submit the form
        this.submit();
      } else {
        // Display an error message
        alert('Please select a file');
      }
    });
  });
  