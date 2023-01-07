window.onload = function () {
    const flashcardElement = document.getElementById('flashcard');
    const flashcardInnerElement = document.getElementById('flashcard-inner');
    const frontElement = document.getElementById('front');
    const backElement = document.getElementById('back');
    const nextButton = document.getElementById('next-button');

    let showingBack = false;

    function updateFlashcard(flashcard) {
        frontElement.innerHTML = flashcard.front;
        backElement.innerHTML = flashcard.back;
        showingBack = false;
        backElement.style.display = 'none';
    }

    function getNextFlashcard() {
        const form = document.querySelector('form');
        const formData = new FormData(form);
        const selectedChapters = [];
        for (const [key, value] of formData.entries()) {
            selectedChapters.push(value);
        }
        const options = {
            method: 'POST',
            body: JSON.stringify({chapters: selectedChapters}),
            headers: {'Content-Type': 'application/json'}
        };
        fetch('/api/next-flashcard', options)
            .then(response => response.json())
            .then(updateFlashcard);
    }

    nextButton.addEventListener('click', function () {
        if (showingBack) {
            getNextFlashcard();
        } else {
            showingBack = true;
            backElement.style.display = 'block';
        }
    });

    getNextFlashcard();

};





