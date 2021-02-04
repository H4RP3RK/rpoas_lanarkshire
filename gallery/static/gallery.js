// Toggles filter buttons and modal

function toggle(elName) {
    const el = document.querySelector(`#${elName}`);
    const displayList = el.nextElementSibling;
    displayList.classList.toggle('closed');
}

// Modal arrows

function nextImage(openModal) {
    const modal = document.querySelector(`#${openModal}`);
    const nextModal = modal.nextElementSibling.nextElementSibling;
    modal.classList.add('closed');
    nextModal.classList.toggle('closed');
}

function previousImage(openModal) {
    const modal = document.querySelector(`#${openModal}`);
    const previousModal = modal.previousElementSibling.previousElementSibling;
    modal.classList.add('closed');
    previousModal.classList.toggle('closed');
}