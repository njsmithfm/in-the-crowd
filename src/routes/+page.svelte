<script>
  import PageHeader from "#lib/components/PageHeader.svelte";
  import ArchiveView from "#lib/components/ArchiveView.svelte";
  import AnalysisDashboard from "#lib/components/analysis/AnalysisDashboard.svelte";
  let viewMode = $state("archive");
  let { data } = $props();
  const setViewMode = (mode) => {
    viewMode = mode;
    if (typeof window !== "undefined") {
      window.scrollTo({ top: 0, behavior: "auto" });
    }
  };
</script>

<PageHeader {viewMode} onChangeView={setViewMode} />

<main class="view-content">
  {#key viewMode}
    {#if viewMode === "archive"}
      <ArchiveView />
    {:else}
      <AnalysisDashboard />
    {/if}
  {/key}
</main>

<style>
  .view-content {
    display: block;
    width: 100%;
  }
</style>
