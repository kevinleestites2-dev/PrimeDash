
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PANTHEON | MISSION CONTROL</title>
    <script src="[https://cdn.tailwindcss.com](https://cdn.tailwindcss.com)"></script>
    <link href="[https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap](https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap)" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
        .card { background-color: #161b22; border: 1px solid #30363d; border-radius: 12px; }
        .metric-val { color: #58a6ff; font-weight: 700; font-size: 2.5rem; line-height: 1; }
        .status-dot { height: 10px; width: 10px; background-color: #3fb950; border-radius: 50%; display: inline-block; margin-right: 8px; }
        .sidebar-item { cursor: pointer; transition: 0.2s; }
        .sidebar-item:hover { background-color: #21262d; }
        .active-item { background-color: #21262d; border-left: 4px solid #58a6ff; }
    </style>
</head>
<body class="flex flex-col md:flex-row h-screen">
    <!-- Sidebar -->
    <div class="w-full md:w-64 bg-[#161b22] border-r border-[#30363d] overflow-y-auto">
        <div class="p-6 border-b border-[#30363d]">
            <h1 class="text-xl font-bold tracking-widest text-[#f0f6fc]">PANTHEON</h1>
            <p class="text-xs text-gray-500 mt-1">FORGEMASTER_AUTHORIZED</p>
        </div>
        <nav id="bot-list" class="mt-4">
            <!-- Bot items will be injected here -->
        </nav>
    </div>

    <!-- Main Content -->
    <div class="flex-1 overflow-y-auto p-6 md:p-12">
        <div class="flex justify-between items-start mb-8">
            <div>
                <h2 id="bot-name" class="text-5xl font-bold text-[#f0f6fc]">MidasPrime</h2>
                <div class="mt-2 flex items-center">
                    <span class="status-dot"></span>
                    <span id="bot-role" class="text-gray-400 font-semibold uppercase tracking-wider">Treasury Manager</span>
                </div>
            </div>
            <button onclick="location.reload()" class="bg-[#21262d] border border-[#30363d] px-4 py-2 rounded-md hover:bg-[#30363d] transition">REFRESH SIGNAL</button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div class="card p-6">
                <p id="m1-label" class="text-sm text-gray-400 mb-2">Total Value</p>
                <p id="m1-val" class="metric-val">$14,202.40</p>
            </div>
            <div class="card p-6">
                <p id="m2-label" class="text-sm text-gray-400 mb-2">Yield</p>
                <p id="m2-val" class="metric-val">+2.4%</p>
            </div>
            <div class="card p-6">
                <p id="m3-label" class="text-sm text-gray-400 mb-2">Withdrawal</p>
                <p id="m3-val" class="metric-val">4h 20m</p>
            </div>
        </div>

        <div class="card p-8">
            <h3 class="text-lg font-bold mb-4 border-b border-[#30363d] pb-2">◈ OPERATIONAL OVERVIEW</h3>
            <p id="bot-desc" class="text-gray-300 leading-relaxed">Orchestrating arbitrage loops across Alpha nodes and managing decentralized treasury growth.</p>
        </div>

        <div class="mt-8 text-center text-gray-600 text-xs tracking-widest uppercase">
            Sovereign Engine v3.0 // No Limits
        </div>
    </div>

    <script>
        const BOTS = {
            "MidasPrime": { role: "Treasury Manager", desc: "Orchestrating arbitrage loops across Alpha nodes.", m: ["Total Value", 14202.40, "$", "Yield", 2.4, "%", "Withdrawal", "4h 20m"] },
            "Prometheus": { role: "Autonomous Catalyst", desc: "Scanning sub-networks for expansion catalysts.", m: ["Compute", 84.2, "%", "Nodes", 42, "", "Neural Sync", "99.8%"] },
            "NexusPrime": { role: "Mobile Bridge", desc: "High-fidelity link to the Red Magic 10 Pro.", m: ["Latency", 8, "ms", "RAM Usage", 2.4, "GB", "Uptime", "14h 22m"] },
            "OrionPrime": { role: "Resource Hunter", desc: "Identifying and acquiring high-signal targets.", m: ["Hunts", 182, "", "Conversion", 4.2, "%", "New Leads", "4"] }
        };

        // Populate sidebar
        const list = document.getElementById('bot-list');
        Object.keys(BOTS).forEach(name => {
            const div = document.createElement('div');
            div.className = `sidebar-item p-4 border-b border-[#30363d] ${name === 'MidasPrime' ? 'active-item' : ''}`;
            div.innerHTML = `<span class="font-bold">${name}</span>`;
            div.onclick = () => selectBot(name, div);
            list.appendChild(div);
        });

        function selectBot(name, el) {
            document.querySelectorAll('.sidebar-item').forEach(i => i.classList.remove('active-item'));
            el.classList.add('active-item');
            
            const bot = BOTS[name];
            document.getElementById('bot-name').innerText = name;
            document.getElementById('bot-role').innerText = bot.role;
            document.getElementById('bot-desc').innerText = bot.desc;
            
            document.getElementById('m1-label').innerText = bot.m[0];
            document.getElementById('m1-val').innerText = `\({bot.m[2]}\){bot.m[1]}`;
            document.getElementById('m2-label').innerText = bot.m[3];
            document.getElementById('m2-val').innerText = `\({bot.m[4]}\){bot.m[5]}`;
            document.getElementById('m3-label').innerText = bot.m[6];
            document.getElementById('m3-val').innerText = bot.m[7];
        }

        // Simulating live data drift
        setInterval(() => {
            const m1 = document.getElementById('m1-val');
            if (m1.innerText.includes('$')) {
                let val = parseFloat(m1.innerText.replace('$', '').replace(',', ''));
                val += (Math.random() - 0.5) * 2;
                m1.innerText = '$' + val.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            }
        }, 3000);
    </script>
</body>
</html>
