<script>
  import BaseChartPanel from "$lib/components/analysis/charts/BaseChartPanel.svelte";

  let { data = [] } = $props();
</script>

<BaseChartPanel
  title="Timeline"
  subtitle="Shows per year so you can see the shape of the archive"
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
