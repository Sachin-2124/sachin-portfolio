document.addEventListener('DOMContentLoaded', () => {
  initCoreLoader();
  initSmoothSlowOrbit();
  initParticleCanvas();
  initThwipEffect();
  initAudioSynth();
  initEducationFilters();
  initContactForm();
  initNavScroll();
  initModals();
});

/* ==========================================================================
   0.1 Smooth Slow Upright Orbit (Never Ulta / Straight Text / Easy Click)
   ========================================================================== */
function initSmoothSlowOrbit() {
  const container = document.querySelector('.orbit-container');
  const badgeWA = document.querySelector('.orbit-badge.whatsapp');
  const badgeLI = document.querySelector('.orbit-badge.linkedin');
  const badgePhone = document.querySelector('.orbit-badge.call');
  const badgeGH = document.querySelector('.orbit-badge.github');

  if (!container || !badgeWA || !badgeLI || !badgePhone || !badgeGH) return;

  const isMobile = window.innerWidth < 768;
  const radius = isMobile ? 140 : 175;

  let angle = 0;
  let isPaused = false;
  let hoveredBadge = null;

  // Pause when hovering over the container or any badge
  container.addEventListener('mouseenter', () => (isPaused = true));
  container.addEventListener('mouseleave', () => {
    isPaused = false;
    hoveredBadge = null;
  });
  container.addEventListener('touchstart', () => (isPaused = true), { passive: true });
  container.addEventListener('touchend', () => {
    setTimeout(() => { isPaused = false; }, 1000);
  }, { passive: true });

  const badges = [
    { el: badgeLI, offset: -Math.PI / 2 },          // Top
    { el: badgeWA, offset: 0 },                     // Right
    { el: badgeGH, offset: Math.PI / 2 },          // Bottom
    { el: badgePhone, offset: Math.PI }            // Left
  ];

  badges.forEach((b) => {
    b.el.addEventListener('mouseenter', () => {
      hoveredBadge = b.el;
      isPaused = true;
    });
    b.el.addEventListener('mouseleave', () => {
      if (hoveredBadge === b.el) hoveredBadge = null;
    });
  });

  function renderOrbit() {
    if (!isPaused) {
      angle += 0.0035; // Gentle slow revolving speed
      if (angle >= Math.PI * 2) angle -= Math.PI * 2;
    }

    badges.forEach((b) => {
      const curAngle = angle + b.offset;
      const x = Math.cos(curAngle) * radius;
      const y = Math.sin(curAngle) * radius;
      const scale = (hoveredBadge === b.el) ? 1.1 : 1.0;
      b.el.style.transform = `translate(${x}px, ${y}px) translate(-50%, -50%) scale(${scale})`;
    });

    requestAnimationFrame(renderOrbit);
  }

  renderOrbit();
}

/* ==========================================================================
   0. Cyber Core Initialization Loading Screen Animation
   ========================================================================== */
function initCoreLoader() {
  const loader = document.getElementById('core-loader');
  const percentText = document.getElementById('loader-percentage');
  const fillBar = document.getElementById('loader-fill');

  if (!loader || !percentText || !fillBar) return;

  let progress = 0;
  const duration = 1400; // ms
  const interval = 20; // ms
  const step = 100 / (duration / interval);

  const timer = setInterval(() => {
    progress += step;
    if (progress >= 100) {
      progress = 100;
      clearInterval(timer);
      percentText.textContent = '100% / 100';
      fillBar.style.width = '100%';

      setTimeout(() => {
        loader.classList.add('loader-hidden');
        setTimeout(() => {
          loader.style.display = 'none';
        }, 600);
      }, 350);
    } else {
      const current = Math.floor(progress);
      percentText.textContent = `${current}% / 100`;
      fillBar.style.width = `${current}%`;
    }
  }, interval);
}

/* ==========================================================================
   1. Interactive Spider Particle Web Canvas
   ========================================================================== */
function initParticleCanvas() {
  const canvas = document.getElementById('bg-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  const mouse = { x: null, y: null, radius: 150 };

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  window.addEventListener('mouseleave', () => {
    mouse.x = null;
    mouse.y = null;
  });

  // Particle constructor
  const numParticles = Math.min(Math.floor((width * height) / 14000), 75);
  const particles = [];

  class Particle {
    constructor() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.size = Math.random() * 2 + 1;
      this.vx = (Math.random() - 0.5) * 0.7;
      this.vy = (Math.random() - 0.5) * 0.7;
      this.color = Math.random() > 0.3 ? '#ef4444' : '#38bdf8';
    }

    update() {
      this.x += this.vx;
      this.y += this.vy;

      if (this.x < 0 || this.x > width) this.vx *= -1;
      if (this.y < 0 || this.y > height) this.vy *= -1;

      // Mouse attraction / interaction
      if (mouse.x !== null && mouse.y !== null) {
        const dx = mouse.x - this.x;
        const dy = mouse.y - this.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < mouse.radius) {
          const force = (mouse.radius - dist) / mouse.radius;
          this.x += (dx / dist) * force * 1.5;
          this.y += (dy / dist) * force * 1.5;
        }
      }
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = this.color;
      ctx.shadowBlur = 8;
      ctx.shadowColor = this.color;
      ctx.fill();
      ctx.shadowBlur = 0;
    }
  }

  for (let i = 0; i < numParticles; i++) {
    particles.push(new Particle());
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);

    // Connect particles with spider web lines
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 125) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          const opacity = (1 - dist / 125) * 0.25;
          ctx.strokeStyle = `rgba(239, 68, 68, ${opacity})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }

    particles.forEach((p) => {
      p.update();
      p.draw();
    });

    requestAnimationFrame(animate);
  }

  animate();
}

/* ==========================================================================
   2. Spider Web "THWIP!" Click Shooting Effect
   ========================================================================== */
function initThwipEffect() {
  const canvas = document.getElementById('thwip-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  const webBursts = [];

  class WebShot {
    constructor(targetX, targetY) {
      this.targetX = targetX;
      this.targetY = targetY;
      this.origins = [
        { x: 0, y: height },
        { x: width, y: height },
        { x: width / 2, y: height },
      ];
      this.life = 1.0;
      this.radius = 0;
      this.maxRadius = 35;
    }

    update() {
      this.life -= 0.035;
      this.radius += 1.5;
    }

    draw() {
      if (this.life <= 0) return;

      // Draw web lines shooting from bottom corners
      this.origins.forEach((org) => {
        ctx.beginPath();
        ctx.moveTo(org.x, org.y);
        ctx.lineTo(this.targetX, this.targetY);
        ctx.strokeStyle = `rgba(255, 255, 255, ${this.life * 0.7})`;
        ctx.lineWidth = 1.8 * this.life;
        ctx.stroke();
      });

      // Draw web impact ring at click location
      ctx.beginPath();
      ctx.arc(this.targetX, this.targetY, this.radius, 0, Math.PI * 2);
      ctx.strokeStyle = `rgba(239, 68, 68, ${this.life * 0.9})`;
      ctx.lineWidth = 2;
      ctx.stroke();

      // Spider Web radial spikes
      const numSpikes = 8;
      for (let s = 0; s < numSpikes; s++) {
        const angle = (s * Math.PI * 2) / numSpikes;
        ctx.beginPath();
        ctx.moveTo(this.targetX, this.targetY);
        ctx.lineTo(
          this.targetX + Math.cos(angle) * (this.radius * 1.4),
          this.targetY + Math.sin(angle) * (this.radius * 1.4)
        );
        ctx.strokeStyle = `rgba(244, 63, 94, ${this.life * 0.8})`;
        ctx.lineWidth = 1;
        ctx.stroke();
      }
    }
  }

  document.addEventListener('click', (e) => {
    // Avoid triggering when clicking form inputs or buttons directly
    if (['INPUT', 'TEXTAREA', 'BUTTON', 'A'].includes(e.target.tagName)) return;
    webBursts.push(new WebShot(e.clientX, e.clientY));
  });

  function renderThwips() {
    ctx.clearRect(0, 0, width, height);

    for (let i = webBursts.length - 1; i >= 0; i--) {
      webBursts[i].update();
      webBursts[i].draw();
      if (webBursts[i].life <= 0) {
        webBursts.splice(i, 1);
      }
    }
    requestAnimationFrame(renderThwips);
  }

  renderThwips();
}

/* ==========================================================================
   3. Spider-Man Theme (Heroic Brass & Cyber-Hero Beat) Audio Synthesizer
   ========================================================================== */
function initAudioSynth() {
  const toggleBtn = document.getElementById('sound-toggle-btn');
  const songTitle = document.getElementById('song-title');
  const eqBars = document.querySelectorAll('.equalizer-bar');

  if (!toggleBtn) return;

  let audioCtx = null;
  let isPlaying = false;
  let timerId = null;
  let activeNodes = [];
  let masterGain = null;

  // Frequencies in Hz for Spider-Man Theme (Key of D Minor / Swing Hero)
  const N = {
    D2: 73.42, F2: 87.31, G2: 98.00, A2: 110.00, Bb2: 116.54, C3: 130.81,
    D3: 146.83, E3: 164.81, F3: 174.61, G3: 196.00, Ab3: 207.65, A3: 220.00, Bb3: 233.08, C4: 261.63,
    D4: 293.66, E4: 329.63, F4: 349.23, G4: 392.00, Ab4: 415.30, A4: 440.00, Bb4: 466.16, C5: 523.25,
    D5: 587.33, E5: 659.25, F5: 698.46, G5: 783.99, A5: 880.00
  };

  // Iconic Spider-Man Theme Score (Classic Melody + Pararara Horn Riffs)
  const scoreSpiderMan = [
    // Intro Drum Roll & Heroic Brass Hit
    { lead: N.D4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.18, drum: 'kick' },
    { lead: N.D4, chord: null, bass: N.D2, dur: 0.18, drum: 'snare' },
    { lead: N.F4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.22, drum: 'snare' },
    { lead: N.A4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.45, drum: 'kick' },
    { lead: null, chord: null, bass: null, dur: 0.12, drum: null },

    // Line 1: "Spi-der-Man, Spi-der-Man..."
    { lead: N.D4, chord: [N.F3, N.A3, N.D4], bass: N.D3, dur: 0.28, drum: 'kick' },
    { lead: N.F4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.28, drum: null },
    { lead: N.A4, chord: [N.F3, N.A3, N.D4], bass: N.D3, dur: 0.58, drum: 'snare' },
    { lead: null, chord: null, bass: null, dur: 0.12, drum: null },

    // "...Does what-ev-er a spi-der can"
    { lead: N.A4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.22, drum: 'kick' },
    { lead: N.G4, chord: null, bass: N.F2, dur: 0.22, drum: null },
    { lead: N.F4, chord: [N.F3, N.A3, N.D4], bass: N.G2, dur: 0.22, drum: 'snare' },
    { lead: N.D4, chord: null, bass: N.A2, dur: 0.22, drum: null },
    { lead: N.F4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.22, drum: 'kick' },
    { lead: N.G4, chord: null, bass: N.F2, dur: 0.22, drum: null },
    { lead: N.F4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.60, drum: 'snare' },
    { lead: null, chord: null, bass: null, dur: 0.15, drum: null },

    // Line 2: "Spins a web, an-y size..." (G Minor shift)
    { lead: N.G4, chord: [N.G3, N.Bb3, N.D4], bass: N.G2, dur: 0.28, drum: 'kick' },
    { lead: N.Bb4, chord: [N.G3, N.Bb3, N.D4], bass: N.G3, dur: 0.28, drum: null },
    { lead: N.D5, chord: [N.G3, N.Bb3, N.D4], bass: N.G2, dur: 0.58, drum: 'snare' },
    { lead: null, chord: null, bass: null, dur: 0.12, drum: null },

    // "...Catch-es thieves just like flies"
    { lead: N.D5, chord: [N.G3, N.Bb3, N.D4], bass: N.G2, dur: 0.22, drum: 'kick' },
    { lead: N.C5, chord: null, bass: N.A2, dur: 0.22, drum: null },
    { lead: N.Bb4, chord: [N.G3, N.Bb3, N.D4], bass: N.Bb2, dur: 0.22, drum: 'snare' },
    { lead: N.G4, chord: null, bass: N.C3, dur: 0.22, drum: null },
    { lead: N.Bb4, chord: [N.G3, N.Bb3, N.D4], bass: N.G2, dur: 0.22, drum: 'kick' },
    { lead: N.C5, chord: null, bass: N.A2, dur: 0.22, drum: null },
    { lead: N.Bb4, chord: [N.G3, N.Bb3, N.D4], bass: N.G2, dur: 0.60, drum: 'snare' },
    { lead: null, chord: null, bass: null, dur: 0.15, drum: null },

    // Line 3: Chromatic Hero Climb ("Look out! Here comes the...")
    { lead: N.D4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.18, drum: 'kick' },
    { lead: N.F4, chord: null, bass: N.D2, dur: 0.18, drum: null },
    { lead: N.G4, chord: [N.F3, N.A3, N.D4], bass: N.F2, dur: 0.18, drum: 'snare' },
    { lead: N.Ab4, chord: [N.F3, N.Ab3, N.D4], bass: N.Ab2, dur: 0.18, drum: null },
    { lead: N.A4, chord: [N.E3, N.A3, N.C4], bass: N.A2, dur: 0.35, drum: 'kick' },
    { lead: N.D5, chord: [N.F3, N.A3, N.D4], bass: N.D3, dur: 0.55, drum: 'snare' },

    // "...Spi - der - Man!"
    { lead: N.C5, chord: [N.E3, N.A3, N.C4], bass: N.A2, dur: 0.25, drum: 'kick' },
    { lead: N.A4, chord: [N.F3, N.A3, N.D4], bass: N.F2, dur: 0.25, drum: null },
    { lead: N.F4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.30, drum: 'snare' },
    { lead: N.D4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.85, drum: 'kick' },
    { lead: null, chord: null, bass: null, dur: 0.15, drum: null },

    // Iconic "Pa-ra-ra-ra-ra" Action Brass Riff
    { lead: N.F4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.16, drum: 'kick' },
    { lead: N.G4, chord: null, bass: N.D2, dur: 0.16, drum: null },
    { lead: N.Ab4, chord: null, bass: N.D2, dur: 0.16, drum: 'snare' },
    { lead: N.A4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.30, drum: 'kick' },
    { lead: N.C5, chord: [N.E3, N.G3, N.C4], bass: N.C3, dur: 0.22, drum: null },
    { lead: N.A4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.50, drum: 'snare' },

    { lead: N.D4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.15, drum: 'kick' },
    { lead: N.D4, chord: null, bass: N.D2, dur: 0.15, drum: null },
    { lead: N.F4, chord: [N.F3, N.A3, N.D4], bass: N.F2, dur: 0.18, drum: 'snare' },
    { lead: N.G4, chord: [N.G3, N.Bb3, N.D4], bass: N.G2, dur: 0.22, drum: null },
    { lead: N.D4, chord: [N.F3, N.A3, N.D4], bass: N.D2, dur: 0.80, drum: 'kick' },
    { lead: null, chord: null, bass: null, dur: 0.35, drum: null }
  ];

  function getAudioContext() {
    if (!audioCtx) {
      const AudioCtxClass = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AudioCtxClass();
      masterGain = audioCtx.createGain();
      masterGain.gain.setValueAtTime(0.40, audioCtx.currentTime);
      masterGain.connect(audioCtx.destination);
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    return audioCtx;
  }

  // Heroic Punchy Brass Lead (Sawtooth + Lowpass + Fast Attack)
  function playBrassLead(freq, startTime, duration, vol = 0.26) {
    if (!audioCtx || !freq) return;

    const osc = audioCtx.createOscillator();
    const oscSub = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();

    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(freq, startTime);

    // Subtle detuned dual oscillator for big cinematic brass
    oscSub.type = 'triangle';
    oscSub.frequency.setValueAtTime(freq * 0.998, startTime);

    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(3200, startTime);
    filter.frequency.exponentialRampToValueAtTime(1200, startTime + duration);

    // Punchy brass attack envelope
    gain.gain.setValueAtTime(0.001, startTime);
    gain.gain.exponentialRampToValueAtTime(vol, startTime + 0.025);
    gain.gain.setValueAtTime(vol * 0.85, startTime + duration * 0.7);
    gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

    osc.connect(filter);
    oscSub.connect(filter);
    filter.connect(gain);
    gain.connect(masterGain);

    osc.start(startTime);
    oscSub.start(startTime);
    osc.stop(startTime + duration + 0.05);
    oscSub.stop(startTime + duration + 0.05);

    activeNodes.push(osc, oscSub);
  }

  // Comic Organ Chords
  function playOrganChord(chordNotes, startTime, duration, vol = 0.10) {
    if (!audioCtx || !chordNotes) return;

    chordNotes.forEach((f) => {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      const filter = audioCtx.createBiquadFilter();

      osc.type = 'square';
      osc.frequency.setValueAtTime(f, startTime);

      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(1100, startTime);

      gain.gain.setValueAtTime(0.001, startTime);
      gain.gain.exponentialRampToValueAtTime(vol, startTime + 0.03);
      gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration * 0.9);

      osc.connect(filter);
      filter.connect(gain);
      gain.connect(masterGain);

      osc.start(startTime);
      osc.stop(startTime + duration);
      activeNodes.push(osc);
    });
  }

  // Driving Hero Walking Bass
  function playBass(freq, startTime, duration, vol = 0.22) {
    if (!audioCtx || !freq) return;

    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();

    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(freq, startTime);

    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(480, startTime);

    gain.gain.setValueAtTime(0.001, startTime);
    gain.gain.exponentialRampToValueAtTime(vol, startTime + 0.03);
    gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration * 0.95);

    osc.connect(filter);
    filter.connect(gain);
    gain.connect(masterGain);

    osc.start(startTime);
    osc.stop(startTime + duration);
    activeNodes.push(osc);
  }

  // Action Spy / Hero Drums
  function playDrum(time, type) {
    if (!audioCtx || !type) return;

    if (type === 'snare') {
      const bufferSize = Math.floor(audioCtx.sampleRate * 0.14);
      const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
      const data = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (audioCtx.sampleRate * 0.03));
      }
      const noise = audioCtx.createBufferSource();
      noise.buffer = buffer;

      const filter = audioCtx.createBiquadFilter();
      filter.type = 'bandpass';
      filter.frequency.setValueAtTime(1400, time);

      const gain = audioCtx.createGain();
      gain.gain.setValueAtTime(0.15, time);
      gain.gain.exponentialRampToValueAtTime(0.001, time + 0.14);

      noise.connect(filter);
      filter.connect(gain);
      gain.connect(masterGain);

      noise.start(time);
      activeNodes.push(noise);
    } else if (type === 'kick') {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();

      osc.frequency.setValueAtTime(130, time);
      osc.frequency.exponentialRampToValueAtTime(45, time + 0.10);

      gain.gain.setValueAtTime(0.30, time);
      gain.gain.exponentialRampToValueAtTime(0.001, time + 0.12);

      osc.connect(gain);
      gain.connect(masterGain);

      osc.start(time);
      osc.stop(time + 0.13);
      activeNodes.push(osc);
    }
  }

  function playSpiderManTheme() {
    if (!audioCtx || !isPlaying) return;

    let timeOffset = audioCtx.currentTime + 0.03;

    scoreSpiderMan.forEach((step) => {
      if (step.lead) {
        playBrassLead(step.lead, timeOffset, step.dur, 0.28);
      }
      if (step.chord) {
        playOrganChord(step.chord, timeOffset, step.dur, 0.09);
      }
      if (step.bass) {
        playBass(step.bass, timeOffset, step.dur, 0.22);
      }
      if (step.drum) {
        playDrum(timeOffset, step.drum);
      }

      timeOffset += step.dur;
    });

    const totalDuration = scoreSpiderMan.reduce((sum, s) => sum + s.dur, 0);

    timerId = setTimeout(() => {
      if (isPlaying) {
        playSpiderManTheme();
      }
    }, totalDuration * 1000);
  }

  function stopAllAudio() {
    if (timerId) clearTimeout(timerId);
    activeNodes.forEach((node) => {
      try { node.stop(); } catch (e) {}
    });
    activeNodes = [];
  }

  toggleBtn.addEventListener('click', () => {
    const ctx = getAudioContext();

    if (!isPlaying) {
      isPlaying = true;
      toggleBtn.innerHTML = '<span>🔊</span><span>Music: ON</span>';
      if (songTitle) songTitle.textContent = '🕷️ Spider-Man Theme (Heroic Beat)';
      eqBars.forEach((bar) => (bar.style.animationPlayState = 'running'));
      
      playSpiderManTheme();
    } else {
      isPlaying = false;
      stopAllAudio();
      toggleBtn.innerHTML = '<span>🔇</span><span>Music: Muted</span>';
      if (songTitle) songTitle.textContent = 'Spider-Man Theme (Muted)';
      eqBars.forEach((bar) => (bar.style.animationPlayState = 'paused'));
    }
  });
}

/* ==========================================================================
   4. Education Category Filters
   ========================================================================== */
function initEducationFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const eduCards = document.querySelectorAll('.edu-card');

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      filterBtns.forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      eduCards.forEach((card) => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.style.display = 'flex';
          card.style.opacity = '0';
          card.style.transform = 'translateY(15px)';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 50);
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* ==========================================================================
   5. Contact Form AJAX Handler
   ========================================================================== */
function initContactForm() {
  const form = document.getElementById('contact-form');
  const feedback = document.getElementById('form-feedback');
  if (!form || !feedback) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<span>Sending... 🚀</span>';
    submitBtn.disabled = true;

    const formData = new FormData(form);

    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
        },
      });

      const data = await response.json();

      if (response.ok && data.status === 'success') {
        feedback.className = 'form-feedback success';
        feedback.textContent = data.message;
        form.reset();
      } else {
        feedback.className = 'form-feedback error';
        feedback.textContent = data.message || 'Something went wrong. Please try again.';
      }
    } catch (err) {
      feedback.className = 'form-feedback error';
      feedback.textContent = 'Network error. Please reach out via WhatsApp or email directly.';
    } finally {
      submitBtn.innerHTML = originalText;
      submitBtn.disabled = false;
      setTimeout(() => {
        feedback.style.display = 'none';
      }, 7000);
    }
  });
}

/* ==========================================================================
   6. Navigation & Scroll Highlighter
   ========================================================================== */
function initNavScroll() {
  const navLinks = document.querySelectorAll('.nav-links a');
  const sections = document.querySelectorAll('section[id]');
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mobileDrawer = document.querySelector('.mobile-nav-drawer');
  const scrollTopBtn = document.querySelector('.scroll-top-btn');

  // Mobile menu toggle
  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      mobileDrawer.classList.toggle('open');
    });

    mobileDrawer.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        mobileDrawer.classList.remove('open');
      });
    });
  }

  // Scroll to top button
  if (scrollTopBtn) {
    scrollTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Active section tracker
  window.addEventListener('scroll', () => {
    let scrollY = window.pageYOffset;

    sections.forEach((current) => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120;
      const sectionId = current.getAttribute('id');

      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        navLinks.forEach((link) => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  });
}

/* ==========================================================================
   7. Live Demo Architecture Modal
   ========================================================================== */
function initModals() {
  const modalBackdrop = document.getElementById('project-modal');
  const modalTitle = document.getElementById('modal-title');
  const modalBody = document.getElementById('modal-body');
  const modalClose = document.getElementById('modal-close');

  if (!modalBackdrop) return;

  const projectDetails = {
    tour: {
      title: 'Tour & Travels Management System — Architecture & Details',
      content: `
        <div style="display:flex; flex-direction:column; gap:1rem;">
          <p><strong>System Overview:</strong> A full-featured Tourism & Travel Booking web application developed using Python, Django, and SQLite3.</p>
          <div style="background:rgba(2,6,23,0.7); padding:1rem; border-radius:0.75rem; border:1px solid rgba(255,255,255,0.08);">
            <h4 style="color:#ef4444; margin-bottom:0.5rem;">Core Modules & Architecture:</h4>
            <ul style="padding-left:1.2rem; display:flex; flex-direction:column; gap:0.35rem; font-size:0.85rem;">
              <li><strong>Tour Packages & Itinerary Engine:</strong> Dynamic showcase of destination packages with detailed daily plans, pricing, and hotel details.</li>
              <li><strong>Booking & Reservation Pipeline:</strong> Multi-step booking workflow with date selection, passenger count, and cost breakdown.</li>
              <li><strong>Admin Management Portal:</strong> Django admin & custom dashboards to manage packages, booking statuses, customer inquiries, and driver allocations.</li>
              <li><strong>Billing & Invoices:</strong> Automated PDF / invoice generation and payment records.</li>
            </ul>
          </div>
          <p style="font-size:0.85rem; color:#94a3b8;"><strong>Repository:</strong> <a href="https://github.com/Sachin-2124/tour-and-travels-management-system" target="_blank" style="color:#38bdf8;">github.com/Sachin-2124/tour-and-travels-management-system</a></p>
        </div>
      `,
    },
    smartresume: {
      title: 'SmartResume (AI & Dynamic Resume Builder) — Architecture',
      content: `
        <div style="display:flex; flex-direction:column; gap:1rem;">
          <p><strong>System Overview:</strong> An intelligent Resume Builder and ATS optimization platform built with Python & Django.</p>
          <div style="background:rgba(2,6,23,0.7); padding:1rem; border-radius:0.75rem; border:1px solid rgba(255,255,255,0.08);">
            <h4 style="color:#ef4444; margin-bottom:0.5rem;">Key Capabilities:</h4>
            <ul style="padding-left:1.2rem; display:flex; flex-direction:column; gap:0.35rem; font-size:0.85rem;">
              <li><strong>Interactive Resume Form Builder:</strong> Real-time dynamic input for work experience, education, skills, and projects with live instant preview.</li>
              <li><strong>ATS Compatibility Optimization:</strong> Pre-built formatting layouts that pass Automated Tracking Systems smoothly.</li>
              <li><strong>Multi-Version Resume Storage:</strong> Logged-in users can save and customize different versions of their resumes.</li>
              <li><strong>Instant PDF Export:</strong> Clean backend-driven high-resolution PDF generation ready for job applications.</li>
            </ul>
          </div>
          <p style="font-size:0.85rem; color:#94a3b8;"><strong>Repository:</strong> <a href="https://github.com/Sachin-2124/SmartResume" target="_blank" style="color:#38bdf8;">github.com/Sachin-2124/SmartResume</a></p>
        </div>
      `,
    },
    stadium: {
      title: 'Stadium Management System — Architecture & Details',
      content: `
        <div style="display:flex; flex-direction:column; gap:1rem;">
          <p><strong>System Overview:</strong> An end-to-end Python & Django software suite for venue and match operations.</p>
          <div style="background:rgba(2,6,23,0.7); padding:1rem; border-radius:0.75rem; border:1px solid rgba(255,255,255,0.08);">
            <h4 style="color:#ef4444; margin-bottom:0.5rem;">Core Modules:</h4>
            <ul style="padding-left:1.2rem; display:flex; flex-direction:column; gap:0.35rem; font-size:0.85rem;">
              <li><strong>Event & Match Scheduling:</strong> Calendar organizer for fixtures, pitch allocations, and referee assignments.</li>
              <li><strong>Ticketing & Turnstile Gates:</strong> QR-authenticated ticket booking, seat reservation, and entry management.</li>
              <li><strong>Fan CRM & Feedback:</strong> Fan portal, rating submissions, and match notifications.</li>
              <li><strong>Staff & Security Deployment:</strong> Gate security duties and emergency coordination.</li>
            </ul>
          </div>
          <p style="font-size:0.85rem; color:#94a3b8;"><strong>Tech Stack:</strong> Python, Django, SQLite3, Bootstrap, JavaScript.</p>
        </div>
      `,
    },
    pg: {
      title: 'PG Management System — Architecture & Details',
      content: `
        <div style="display:flex; flex-direction:column; gap:1rem;">
          <p><strong>System Overview:</strong> A complete Paying Guest Accommodation portal built with Django for hostel/PG administrators and tenants.</p>
          <div style="background:rgba(2,6,23,0.7); padding:1rem; border-radius:0.75rem; border:1px solid rgba(255,255,255,0.08);">
            <h4 style="color:#ef4444; margin-bottom:0.5rem;">Key Capabilities:</h4>
            <ul style="padding-left:1.2rem; display:flex; flex-direction:column; gap:0.35rem; font-size:0.85rem;">
              <li><strong>Room & Bed Allocator:</strong> Live matrix showing occupied vs. available beds with instant booking.</li>
              <li><strong>Automated Rent Billing:</strong> Monthly invoice generation, payment history ledger, and pending dues tracker.</li>
              <li><strong>Complaint Desk:</strong> Interactive maintenance issue tracker with admin resolution status.</li>
              <li><strong>Tenant KYC Verification:</strong> Digital storage of tenant identity and agreement records.</li>
            </ul>
          </div>
          <p style="font-size:0.85rem; color:#94a3b8;"><strong>Tech Stack:</strong> Python 3, Django, SQLite3, Bootstrap, Vanilla JavaScript.</p>
        </div>
      `,
    },
  };

  document.querySelectorAll('[data-open-modal]').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const projKey = btn.getAttribute('data-open-modal');
      const data = projectDetails[projKey];
      if (data) {
        modalTitle.textContent = data.title;
        modalBody.innerHTML = data.content;
        modalBackdrop.classList.add('open');
      }
    });
  });

  if (modalClose) {
    modalClose.addEventListener('click', () => {
      modalBackdrop.classList.remove('open');
    });
  }

  modalBackdrop.addEventListener('click', (e) => {
    if (e.target === modalBackdrop) {
      modalBackdrop.classList.remove('open');
    }
  });
}

/**
 * Copy Address helper with visual feedback toast
 */
function copyAddressToClipboard(text) {
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text).then(() => {
      showToast('📍 Address copied to clipboard!');
    }).catch(() => {
      prompt('Copy address manually:', text);
    });
  } else {
    // Fallback
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand('copy');
      showToast('📍 Address copied to clipboard!');
    } catch (err) {
      prompt('Copy address manually:', text);
    }
    document.body.removeChild(textArea);
  }
}

function showToast(msg) {
  let toast = document.getElementById('global-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'global-toast';
    toast.style.cssText = `
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #10b981;
      color: #34d399;
      font-family: var(--font-mono, monospace);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.75rem 1.25rem;
      border-radius: 9999px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      z-index: 999999;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.3s ease;
      opacity: 0;
      transform: translateY(20px);
    `;
    document.body.appendChild(toast);
  }
  toast.innerHTML = msg;
  toast.style.opacity = '1';
  toast.style.transform = 'translateY(0)';
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(20px)';
  }, 3000);
}

