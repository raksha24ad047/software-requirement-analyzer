async function runAnalysis() {
    const input = document.getElementById("ideaInput").value;
    const loading = document.getElementById("loading");
    const resultsSection = document.getElementById("resultsSection");

    if (!input.trim()) {
        alert("Please enter an app idea first.");
        return;
    }

    loading.classList.remove("hidden");
    resultsSection.classList.add("hidden");

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ idea: input })
        });

        const data = await response.json();
        loading.classList.add("hidden");

        if (data.error) {
            alert(data.error);
            return;
        }

        populateList("targetUsers", data.target_users);
        populateList("inputs", data.inputs);
        populateList("outputs", data.outputs);
        populateList("functionalReqs", data.functional_requirements);
        populateList("nonFunctionalReqs", data.non_functional_requirements);
        populateList("constraints", data.constraints);
        populateList("potentialChallenges", data.potential_challenges);

        resultsSection.classList.remove("hidden");
    } catch (err) {
        loading.classList.add("hidden");
        alert("An error occurred while connecting to the server.");
    }
}

function populateList(elementId, items) {
    const listElement = document.getElementById(elementId);
    listElement.innerHTML = "";
    if (items && items.length > 0) {
        items.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            listElement.appendChild(li);
        });
    } else {
        const li = document.createElement("li");
        li.textContent = "None identified.";
        listElement.appendChild(li);
    }
}
