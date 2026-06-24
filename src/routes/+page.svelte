<script>
  import ShowsList from "$lib/components/ShowsList.svelte";
  import ShowDetail from "$lib/components/ShowDetail.svelte";

  let selectedShow = $state(null);

  const handleSelection = (showData) => {
    console.log("Parent received:", showData);
    selectedShow = showData;
  };
</script>

<div>
  <div>
    <!-- Explicitly pass the function -->
    <ShowsList onSelect={handleSelection} />
  </div>

  <div>
    <!-- Pass the object directly -->
    <ShowDetail show={selectedShow} onClose={() => (selectedShow = null)} />
  </div>
</div>
