<script>
  import shows from "../../../public/data/shows.json";

  // Ensure this name matches the parent's key
  let { onSelect } = $props();
</script>

{#each shows as show}
  <button
    onclick={() => {
      console.log("Successful New Artist Selection:", show.Artist);
      if (onSelect) {
        onSelect(show);
      } else {
        console.error("onSelect prop is missing!");
      }
    }}
  >
    <strong>{show.Artist}</strong> at {show.Venue}
  </button>
{/each}
