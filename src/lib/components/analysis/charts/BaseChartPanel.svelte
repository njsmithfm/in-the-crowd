<script>
  let { title, subtitle } = $props();
</script>

<section class="chart-panel">
  <header class="chart-panel-header">
    <h2>{title}</h2>
    {#if subtitle}
      <p>{subtitle}</p>
    {/if}
  </header>

  <div class="chart-panel-body">
    <slot />
  </div>
</section>
