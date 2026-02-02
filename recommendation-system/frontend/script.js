async function getRecommendations() {
    const userId = document.getElementById("userId").value;

    if (!userId) {
        alert("Please enter a User ID");
        return;
    }

    try {
        const response = await fetch(
            `http://127.0.0.1:8000/recommend/${userId}`
        );

        const data = await response.json();

        const container = document.getElementById("movies");
        const title = document.getElementById("sectionTitle");

        container.innerHTML = "";
        title.classList.remove("hidden");

        data.recommended_movies.forEach(movie => {
            const card = document.createElement("div");
            card.className = "movie-card";

            card.innerHTML = `
                <h3>${movie}</h3>
                <span class="badge">Recommended</span>
            `;

            container.appendChild(card);
        });

    } catch (err) {
        alert("Backend not running");
    }
}
