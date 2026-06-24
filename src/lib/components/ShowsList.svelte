<script>
  import shows from "../../../public/data/shows.json";

  // Ensure this name matches the parent's key
  let { onSelect } = $props();
</script>

{#each shows as show}
  <button
    onclick={() => {
      console.log("List button clicked!", show.Artist);
      if (onSelect) {
        onSelect(show);
      } else {
        console.error("onSelect prop is missing!");
      }
    }}
  >
    {show.Artist} - {show.Venue}
  </button>
{/each}
