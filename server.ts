import express from 'express';

const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Persian Morning Bot</title>
      <style>
        body { font-family: system-ui, -apple-system, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f3f4f6; }
        .card { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; max-width: 600px; }
        h1 { color: #1f2937; margin-bottom: 1rem; }
        p { color: #4b5563; line-height: 1.5; }
        .code { background: #e5e7eb; padding: 0.5rem; border-radius: 4px; font-family: monospace; display: block; margin: 1rem 0; }
      </style>
    </head>
    <body>
      <div class="card">
        <h1>🌅 Persian Morning Bot</h1>
        <p>This project is a <strong>Python Telegram Bot</strong> designed to run daily via GitHub Actions.</p>
        <p>Because it's a background worker script, there is no web interface.</p>
        <p>To run the bot locally, use the console:</p>
        <span class="code">export PYTHONPATH=. && python src/main.py</span>
        <p>See the <strong>README.md</strong> for setup instructions and how to deploy to GitHub Actions.</p>
      </div>
    </body>
    </html>
  `);
});

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', type: 'worker-preview' });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Preview server running on port ${PORT}`);
});
