document.getElementById('vendorForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = new FormData(document.getElementById('vendorForm'));

    const res = await fetch('/submit_vendor', {
        method: 'POST',
        body: form
    });
    const data = await res.json();
    document.getElementById('response').innerText = `Submitted! Risk Score: ${data.risk_score}`;
});
