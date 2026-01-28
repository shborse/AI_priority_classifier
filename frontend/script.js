document.getElementById("priorityForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const payload = {
        urgent_score: Number(document.getElementById("urgency").value),
        impact_score: Number(document.getElementById("impact").value),
        affected_users: Number(document.getElementById("affected_users").value),
        delay_hours: Number(document.getElementById("delay_hours").value),
        critical_flag: document.getElementById("critical").checked ? 1 : 0
    };

    try {
        const res = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!res.ok) {
            const err = await res.json();
            throw new Error(err.detail || "Could not connect to API.");
        }

        const data = await res.json();

        const resultBox = document.getElementById("result");
        const decisionText = document.getElementById("decision");
        const confidenceText = document.getElementById("confidence");

        resultBox.className = "result";

        if (data.decision.includes("High")) resultBox.classList.add("high");
        else if (data.decision.includes("Medium")) resultBox.classList.add("medium");
        else resultBox.classList.add("low");

        decisionText.innerText = data.decision;
        confidenceText.innerText = `Confidence: ${(data.confidence * 100).toFixed(2)}%`;

        resultBox.classList.remove("hidden");
    } catch (err) {
        alert(err.message);
    }
});
