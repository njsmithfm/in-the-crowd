<script>
  import ShowsList from "$lib/components/ShowsList.svelte";
  import ShowDetail from "$lib/components/ShowDetail.svelte";

  let selectedShow = $state(null);

  let { data } = $props();

  const handleSelection = (showData) => {
    selectedShow = showData;
  };
</script>

<div style="display: flex; height: 100vh;">
  <div style="flex: 65%; border-right: 1px solid #000; padding: 1rem;">
    <!-- Explicitly pass the function -->
    <ShowsList onSelect={handleSelection} />
  </div>

  <div style="flex: 35%; padding: 1rem;">
    <!-- Pass the object directly -->
    <ShowDetail show={selectedShow} onClose={() => (selectedShow = null)} />
  </div>
</div>
