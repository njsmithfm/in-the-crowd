<script>
  import favicon from "$lib/assets/favicon.png";
  import "@fontsource/public-sans";
  import "@fontsource/public-sans/400.css";
  import "@fontsource/public-sans/400-italic.css";
  let { children } = $props();
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

{@render children()}

<style>
  :global(*) {
    font-family: "Public Sans", sans-serif;
  }
</style>
