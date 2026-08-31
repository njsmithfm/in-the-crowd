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
</section>

{#if tooltip.visible}
  <div
    style="position:fixed;left:{tooltip.x + 10}px;top:{tooltip.y -
      10}px;background:rgba(255,255,255,0.975);border:3px solid {tooltip.borderColor};padding:4px 8px;border-radius:4px;font-size:14px;pointer-events:none;z-index:100"
  >
    {@html tooltip.content}
  </div>
{/if}
