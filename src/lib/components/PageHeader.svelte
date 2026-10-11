<script>
  let { quote, viewMode = "archive", onChangeView = () => {} } = $props();
</script>

<header class="page-header">
  <div class="top-quote">
    <p>{quote}</p>
  </div>
  <div class="site-header">
    <div class="title">
      <h1>In the Crowd</h1>

      <h2>
        <a
          href="?view=archive"
          onclick={(e) => {
            e.preventDefault();
            onChangeView("archive");
          }}
          style:text-decoration={viewMode === "archive"
            ? "rgba(255, 0, 212,0.50) underline"
            : "none"}
          style:color="black">Archive</a
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
    <div class="site-meta">
      <span
        ><a
          href="https://njsmithfm.github.io"
          target="_blank"
          style="text-decoration: none;color: black; font-weight:400; font-size: 1.25rem; font-style: normal;color:#ff00d4"
          >njsmith.fm</a
        >
      </span>
      <p>concerts I've been to since 2022</p>
    </div>
  </div>
</header>

<style>
  .top-quote {
    display: flex;
    justify-content: center;
    background-color: rgba(255, 0, 212, 0.675);
    border-bottom: 2px solid #000;
    color: white;
    font-style: italic;
    font-size: 0.75rem;
  }

  .page-header {
    position: sticky;
    top: 0;
    z-index: 1100;
    background: #fff;
  }

  .top-quote p {
    max-width: 100%;
    margin: 0;
    padding: 0.35rem 1rem;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .site-header {
    display: flex;
    justify-content: space-between;
    border-bottom: 2px solid #000;
  }

  .title {
    display: flex;
    min-width: 0;
    flex-direction: column;
  }

  .title h1 {
    margin: 1.25rem 0 0 1.25rem;
  }

  .title h2 {
    margin: 1rem 0 0.75rem 1.25rem;
  }

  .site-meta {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    padding: 2.5rem 1.5rem 0 1rem;
    text-align: right;
  }

  .site-meta p {
    margin: 0.5rem 0 0;
  }

  @media (max-width: 600px) {
    .title h1 {
      margin: 1rem 0 0 0.75rem;
      font-size: 1.6rem;
    }

    .title h2 {
      margin: 0.7rem 0 0.6rem 0.75rem;
      font-size: 1.1rem;
    }

    .site-meta {
      padding: 1.2rem 0.75rem 0 0.5rem;
    }

    .site-meta p {
      max-width: 9rem;
      font-size: 0.8rem;
    }
  }
</style>
