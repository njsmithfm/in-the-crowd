<script>
  import BaseChartPanel from "$lib/components/analysis/charts/BaseChartPanel.svelte";

  let { data = [] } = $props();
</script>

<BaseChartPanel
  title="Borough comparison"
  subtitle="Where the shows happened most often"
>
  <div class="chart-placeholder">
    {#each data as item}
      <div class="chart-row">
        <span>{item.label}</span>
        <strong>{item.value}</strong>
      </div>
    {/each}
  </div>
</BaseChartPanel>
