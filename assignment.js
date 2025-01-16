// Function to toggle the collapsible menu on smaller screens
function toggleMenu() {
    const leftMenu = document.querySelector('.left-menu');
    leftMenu.classList.toggle('active');
}

// Function to adjust page scale based on screen width
function adjustPageScale() {
    const width = window.innerWidth;

    if (width >= 992 && width <= 1600) {
        document.body.style.transform = 'scale(0.9)';
    } else if (width >= 700 && width <= 767) {
        document.body.style.transform = 'scale(0.8)';
    } else if (width >= 600 && width <= 700) {
        document.body.style.transform = 'scale(0.75)';
    } else if (width <= 600) {
        document.body.style.transform = 'scale(0.5)';
    } else {
        document.body.style.transform = 'scale(1)';
    }
}

// Listen for resize events to adjust the page scale
window.addEventListener('resize', adjustPageScale);

// Call the function initially to set the correct scale on page load
adjustPageScale();
