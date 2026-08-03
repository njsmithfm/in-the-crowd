<script>
  import { page } from "$app/stores";
  let isArchive = $derived($page.url.pathname === "/");
  let isAnalysis = $derived($page.url.pathname === "/analysis");
</script>

<h1>
  <a
    href="/"
    target="_self"
    style:text-decoration={isArchive
      ? " rgba(236, 9, 193,0.50) underline "
      : "none"}
    style:color="black">Archive</a
  >
  &
  <a
    href="./analysis"
    target="_self"
    style:text-decoration={isAnalysis
      ? "rgba(236, 9, 193,0.50) underline"
      : "none"}
    style:color="black">Analysis</a
  >
</h1>
