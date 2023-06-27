document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('nav a');
    const pages = document.querySelectorAll('.page');
  
    links.forEach(function(link) {
      link.addEventListener('click', function(event) {
        event.preventDefault();
        const target = this.getAttribute('href');
  
        // Remove active class from all pages
        pages.forEach(function(page) {
          page.classList.remove('active');
        });
  
        // Add active class to target page
        document.querySelector(target).classList.add('active');
      });
    });
  });