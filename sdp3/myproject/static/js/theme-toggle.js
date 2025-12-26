// Small theme toggle: toggles 'dark' class on <body> and persists choice
(function(){
    const key = 'hospitalms-theme';
    const btn = document.getElementById('theme-toggle');
    const apply = (mode)=>{
        if(mode === 'dark') document.body.classList.add('dark');
        else document.body.classList.remove('dark');
    };
    const setButton = (mode)=>{
        if(!btn) return;
        btn.textContent = mode === 'dark' ? '🌙' : '☀️';
        btn.setAttribute('aria-pressed', mode === 'dark');
        btn.classList.toggle('active', mode === 'dark');
    };

    const stored = localStorage.getItem(key);
    let initial;
    if(stored) initial = stored;
    else if(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) initial = 'dark';
    else initial = 'light';

    apply(initial);
    setButton(initial);

    if(btn){
        btn.addEventListener('click', ()=>{
            const isDark = document.body.classList.toggle('dark');
            const mode = isDark ? 'dark' : 'light';
            localStorage.setItem(key, mode);
            setButton(mode);
        });
    }

    // If user hasn't chosen, respond to system preference changes
    if(!stored && window.matchMedia){
        try{
            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e)=>{
                const sys = e.matches ? 'dark' : 'light';
                apply(sys);
                setButton(sys);
            });
        }catch(e){ /* some browsers use addListener */
            const mq = window.matchMedia('(prefers-color-scheme: dark)');
            if(mq.addListener) mq.addListener((e)=>{
                const sys = e.matches ? 'dark' : 'light';
                apply(sys);
                setButton(sys);
            });
        }
    }
})();
