document.addEventListener("DOMContentLoaded", function () {
    fetch("/dashboard/get_dashboard_data")
        .then(response => response.json())
        .then(data => {
            console.log("Dashboard data received:", data);

            // Update count values
            document.getElementById("bloodCount").innerText = data.blood_donations || 0;
            document.getElementById("organCount").innerText = data.organ_donations || 0;
            document.getElementById("accidentCount").innerText = data.accidents || 0;

            // Prepare data for charts
            const labels = ["Blood Donations", "Organ Donations", "Accidents"];
            const values = [data.blood_donations, data.organ_donations, data.accidents];

            // Adjusting canvas size before rendering charts
            document.getElementById("pieChart").width = 400;
            document.getElementById("pieChart").height = 400;
            document.getElementById("lineChart").width = 600;
            document.getElementById("lineChart").height = 400;

            // PIE CHART
            const pieCtx = document.getElementById("pieChart").getContext("2d");
            new Chart(pieCtx, {
                type: "pie",
                data: {
                    labels: labels,
                    datasets: [{
                        data: values,
                        backgroundColor: ["#FF0000", "#32CD32", "#FFA700"]
                    }]
                },
                options: {
                    responsive: false,  // Disable responsiveness to allow custom size
                    maintainAspectRatio: false
                }
            });

            // LINE CHART
            const lineCtx = document.getElementById("lineChart").getContext("2d");
            new Chart(lineCtx, {
                type: "line",
                data: {
                    labels: ["Day 1", "Day 2", "Day 3"], // Simulated timeline
                    datasets: [
                        {
                            label: "Blood Donations",
                            data: [data.blood_donations - 5, data.blood_donations - 2, data.blood_donations], 
                            borderColor: "#FF0000",
                            fill: false
                        },
                        {
                            label: "Organ Donations",
                            data: [data.organ_donations - 2, data.organ_donations, data.organ_donations + 1], 
                            borderColor: "#32CD32",
                            fill: false
                        },
                        {
                            label: "Accidents",
                            data: [data.accidents - 3, data.accidents, data.accidents + 2], 
                            borderColor: "#FFA700",
                            fill: false
                        }
                    ]
                },
                options: {
                    responsive: false,  
                    maintainAspectRatio: false
                }
            });
        })
        .catch(error => console.error("Fetch error:", error));
});
