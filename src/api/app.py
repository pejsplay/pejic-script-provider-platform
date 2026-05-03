// src/gallery/script.js

// Search functionality with debouncing
let searchInput = document.getElementById('search');
let debounceTimer;

searchInput.addEventListener('input', function() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
        performSearch(searchInput.value);
    }, 300);
});

function performSearch(query) {
    // Implement search logic here
}

// Language filtering
let languages = ['JavaScript', 'Python', 'Bash', 'Go', 'Ruby', 'PHP', 'Java', 'C', 'C++', 'TypeScript', 'SQL', 'YAML', 'JSON', 'XML', 'HTML', 'CSS', 'Rust', 'Kotlin', 'Swift'];

function filterLanguages(selectedLanguages) {
    // Filter logic
}

// Card hover effects
const cards = document.querySelectorAll('.card');
cards.forEach(card => {
    card.addEventListener('mouseover', () => {
        card.classList.add('hover');
    });
    card.addEventListener('mouseout', () => {
        card.classList.remove('hover');
    });
});

// Quick action handlers
function executeAction(id) {
    // Execute logic
}

function editAction(id) {
    // Edit logic
}

function cloneAction(id) {
    // Clone logic
}

function deleteAction(id) {
    // Delete logic
}

// Dynamic grid updates
function updateGrid(data) {
    // Logic to dynamically update grid based on data
}
