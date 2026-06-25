<script>
  import favicon from "$lib/assets/favicon.png";
  import "@fontsource/public-sans";
  import "../app.css";
  let { children } = $props();
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

{@render children()}
