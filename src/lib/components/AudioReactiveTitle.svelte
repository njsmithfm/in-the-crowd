<script>
  import { onMount } from "svelte";
  import { createNoise2D } from "simplex-noise";

  let canvasEl;
  let { artistName = "Artist Name", videoElement } = $props();

  const noise = new createNoise2D();
  let time = 0;
  let audioContext;
  let analyser;
  let dataArray;
  let animationId;

  onMount(() => {
    if (!videoElement) return;

    // Initialize Web Audio API
    audioContext = new (window.AudioContext || window.webkitAudioContext)();
    analyser = audioContext.createAnalyser();
    analyser.fftSize = 256;

    try {
      const source = audioContext.createMediaElementAudioSource(videoElement);
      source.connect(analyser);
      analyser.connect(audioContext.destination);
    } catch (e) {
      console.warn("Could not connect audio source:", e);
    }

    dataArray = new Uint8Array(analyser.frequencyBinCount);
    const ctx = canvasEl.getContext("2d");

    function animate() {
      analyser.getByteFrequencyData(dataArray);
      const amplitude =
        dataArray.reduce((a, b) => a + b) / dataArray.length / 255;

      // Clear canvas
      ctx.fillStyle = "#ffffff";
      ctx.fillRect(0, 0, canvasEl.width, canvasEl.height);

      ctx.font = "bold 72px Arial, sans-serif";
      ctx.fillStyle = "#000000";
      ctx.textBaseline = "middle";

      // Displace each letter based on noise + amplitude
      let x = 50;
      const y = canvasEl.height / 2;

      for (let i = 0; i < artistName.length; i++) {
        const noiseX = noise.noise2D(time + i * 0.2, 0);
        const noiseY = noise.noise2D(time + i * 0.2, 100);

        const offsetX = noiseX * amplitude * 25;
        const offsetY = noiseY * amplitude * 25;

        ctx.save();
        ctx.translate(x + offsetX, y + offsetY);
        ctx.fillText(artistName[i], 0, 0);
        ctx.restore();

        x += ctx.measureText(artistName[i]).width + 8;
      }

      time += 0.05;
      animationId = requestAnimationFrame(animate);
    }

    animate();

    return () => {
      if (animationId) cancelAnimationFrame(animationId);
    };
  });
</script>

<div class="title-container">
  <canvas bind:this={canvasEl} width="900" height="200" class="audio-canvas"
  ></canvas>
</div>

<style>
  .title-container {
    display: flex;
    justify-content: center;
    margin: 2rem 0;
  }

  .audio-canvas {
    max-width: 100%;
    height: auto;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border-radius: 4px;
  }
</style>
