<script>
  import PageHeader from "$lib/components/PageHeader.svelte";
  import ArchiveView from "$lib/components/ArchiveView.svelte";
  import AnalysisDashboard from "$lib/components/analysis/AnalysisDashboard.svelte";
  let viewMode = $state("archive");
  let { data } = $props();
  const setViewMode = (mode) => {
    viewMode = mode;
  };
</script>

<PageHeader quote={data.quote} {viewMode} onChangeView={setViewMode} />

{#if viewMode === "archive"}
  <ArchiveView />
{:else}
  <AnalysisDashboard />
{/if}
