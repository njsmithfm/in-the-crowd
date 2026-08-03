<script>
  import { page } from "$app/stores";
  import PageHeader from "$lib/components/PageHeader.svelte";
  import ShowsList from "$lib/components/ShowsList.svelte";
  import ShowDetail from "$lib/components/ShowDetail.svelte";

  let selectedShow = $state(null);

  const handleSelection = (showData) => {
    console.log("Parent page received:", showData);
    selectedShow = showData;
  };
</script>

<div style="display: flex;  padding: 1rem; border-bottom: 1px solid #000;">
  <PageHeader />
</div>

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
