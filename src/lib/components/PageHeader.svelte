<script>
  let { quote, viewMode = "archive", onChangeView = () => {} } = $props();
</script>

<div class="top-quote" style="display:flex;justify-content: center; ">
  <p>{quote}</p>
</div>
<div
  style="display: flex; flex-direction: row; border-bottom: 2px solid #000; justify-content: space-between;"
>
  <div class="title" style="display: flex; flex-direction: column;">
    <h1 style="margin: 1.25rem 0 0 1.25rem; ">In the Crowd</h1>

    <h2 style="margin: 1rem 0 0.75rem 1.25rem; ">
      <a
        href="?view=archive"
        onclick={(e) => {
          e.preventDefault();
          onChangeView("archive");
        }}
        style:text-decoration={viewMode === "archive"
          ? "rgba(255, 0, 212,0.50) underline"
          : "none"}
        style:color="black"
        Archive>Archive</a
      >
      &
      <a
        href="?view=analysis"
        onclick={(e) => {
          e.preventDefault();
          onChangeView("analysis");
        }}
        style:text-decoration={viewMode === "analysis"
          ? "rgba(255, 0, 212,0.50) underline"
          : "none"}
        style:color="black">Analysis</a
      >
    </h2>
  </div>
  <div style="display: flex; flex-direction: column;align-items:end">
    <span style="margin:2.5rem 1.5rem 0 0"
      ><a
        href="https://njsmithfm.github.io"
        target="_blank"
        style="text-decoration: none;color: black; font-weight:400; font-size: 1.25rem; font-style: normal;color:#ff00d4"
        >njsmith.fm</a
      >
    </span>
    <p style="margin-right:1.5rem;margin-top:0.5rem;">
      documenting the shows I've been to since 2022
    </p>
  </div>
</div>

<style>
  .top-quote {
    background-color: rgba(255, 0, 212, 0.675);
    border-bottom: 2px solid #000;
    color: white;
    font-style: italic;
    font-size: 0.75rem;
  }
</style>
