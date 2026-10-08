<script>
  let { title, subtitle, children } = $props();
  let tooltip = $state({
    visible: false,
    x: 0,
    y: 0,
    content: "",
    borderColor: "#333",
  });

  function showTooltip(e, content, borderColor = "#333") {
    tooltip = {
      visible: true,
      x: e.clientX,
      y: e.clientY,
      content,
      borderColor,
    };
  }
  function hideTooltip() {
    tooltip.visible = false;
  }
</script>

<section class="chart-panel">
  <header class="chart-panel-header">
    <h2>{title}</h2>
    {#if subtitle}<p>{subtitle}</p>{/if}
  </header>
  <div class="chart-panel-body">
    {@render children?.(showTooltip, hideTooltip)}
  </div>

  <style>
    .chart-panel {
      display: flex;
      min-width: 0;
      height: 100%;
      flex-direction: column;
      border: 1px solid #000;
      background: #fff;
    }

    .chart-panel-header {
      padding: 0.8rem 1rem 0;
    }

    .chart-panel-header h2 {
      margin: 0;
      font-size: clamp(1rem, 1.8vw, 1.35rem);
    }

    .chart-panel-header p {
      margin: 0.25rem 0 0;
      font-size: 0.85rem;
    }

    .chart-panel-body {
      display: flex;
      min-width: 0;
      min-height: 0;
      flex: 1;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      padding: clamp(0.5rem, 2vw, 1rem);
    }

    .chart-panel-body :global(svg) {
      display: block;
      width: 100%;
      max-width: 100%;
      height: auto;
    }

    @media (max-width: 600px) {
      .chart-panel-header {
        padding: 0.7rem 0.75rem 0;
      }

      .chart-panel-body {
        padding: 0.5rem;
      }
    }
  </style>
</section>

{#if tooltip.visible}
  <div
    style="position:fixed;left:{tooltip.x + 10}px;top:{tooltip.y -
      10}px;background:rgba(255,255,255,0.975);border:3px solid {tooltip.borderColor};padding:4px 8px;border-radius:4px;font-size:14px;pointer-events:none;z-index:100"
  >
    {@html tooltip.content}
  </div>
{/if}
