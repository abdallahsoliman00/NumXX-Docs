const menuToggle = document.getElementById('menuToggle');
const sidebar = document.getElementById('sidebar');
const sidebarLinks = document.querySelectorAll('.sidebar-menu a');
const contentSections = document.querySelectorAll('.content-section');

// Toggle sidebar
menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('open');
    menuToggle.classList.toggle('shifted');
});

const closeSidebar = () => {
    sidebar.classList.remove('open');
    menuToggle.classList.remove('shifted');
};

// Switch content sections
sidebarLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();

        // Remove active class from all links and sections
        sidebarLinks.forEach(l => l.classList.remove('active'));
        contentSections.forEach(s => s.classList.remove('active'));

        // Add active class to clicked link
        link.classList.add('active');

        // Show corresponding section
        const sectionId = link.getAttribute('data-section');
        document.getElementById(sectionId).classList.add('active');

        // Re-highlight code in the new section
        document.querySelectorAll(`#${sectionId} pre code`).forEach((block) => {
            hljs.highlightElement(block);
        });

        // Add copy buttons to code blocks in the new section
        if (typeof addCopyButtons === 'function') {
            addCopyButtons();
        }

        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });

        // Close sidebar on mobile
        if (window.innerWidth <= 768) {
            closeSidebar();
        }
    });
});