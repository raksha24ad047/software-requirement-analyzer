async function analyzeRequirement() {

    const requirementInput = document.getElementById("requirement");
    const resultContent = document.getElementById("resultContent");

    const requirement = requirementInput.value.trim();

    if (!requirement) {
        resultContent.innerHTML = `
            <p>Please enter a software requirement first.</p>
        `;
        return;
    }

    resultContent.innerHTML = `
        <p>🔍 Analyzing requirement...</p>
    `;

    try {

        const response = await fetch("/analyze", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                requirement: requirement
            })
        });

        const data = await response.json();

        if (!response.ok) {
            resultContent.innerHTML = `
                <p>${data.error}</p>
            `;
            return;
        }

        displayResults(data);

    } catch (error) {

        resultContent.innerHTML = `
            <p>Something went wrong while analyzing the requirement.</p>
        `;

        console.error(error);
    }
}


function displayResults(data) {

    const resultContent = document.getElementById("resultContent");


    const createList = (items) => {

        if (!items || items.length === 0) {
            return "<li>None identified</li>";
        }

        return items.map(item => `<li>${item}</li>`).join("");
    };


    resultContent.innerHTML = `

        <div class="result-grid">

            <div class="result-card">
                <h3>👤 Users / Actors</h3>
                <ul>
                    ${createList(data.users)}
                </ul>
            </div>


            <div class="result-card">
                <h3>⚙️ Functional Requirements</h3>
                <ul>
                    ${createList(data.functional_requirements)}
                </ul>
            </div>


            <div class="result-card">
                <h3>🛡️ Non-Functional Requirements</h3>
                <ul>
                    ${createList(data.non_functional_requirements)}
                </ul>
            </div>


            <div class="result-card">
                <h3>📥 Inputs</h3>
                <ul>
                    ${createList(data.inputs)}
                </ul>
            </div>


            <div class="result-card">
                <h3>📤 Outputs</h3>
                <ul>
                    ${createList(data.outputs)}
                </ul>
            </div>


            <div class="result-card">
                <h3>⚠️ Missing Information</h3>
                <ul>
                    ${createList(data.missing_information)}
                </ul>
            </div>


            <div class="result-card">

                <h3>⭐ Priority</h3>

                <span class="priority">
                    ${data.priority}
                </span>

            </div>

        </div>
    `;
}
