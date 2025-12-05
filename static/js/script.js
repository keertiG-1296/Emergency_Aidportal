// Function to toggle the search bar visibility
function toggleSearch() {
    const searchBar = document.getElementById('searchBar');
    searchBar.style.display = searchBar.style.display === 'block' ? 'none' : 'block';
}

// Function to handle search and scroll to the appropriate section
function searchSection(event) {
    if (event.key === 'Enter') {
        const searchInput = document.getElementById('searchInput').value.toLowerCase();

        // Scroll to the relevant section based on the search term
        if (searchInput.includes("blood donation")) {
            document.getElementById('blood-donation').scrollIntoView({ behavior: 'smooth' });
        } else if (searchInput.includes("accident registry")) {
            document.getElementById('accident-registry').scrollIntoView({ behavior: 'smooth' });
        } else if (searchInput.includes("organ donation")) {
            document.getElementById('organ-donation').scrollIntoView({ behavior: 'smooth' });
        } else {
            alert("Sorry, no matching results found.");
        }
    }
}

