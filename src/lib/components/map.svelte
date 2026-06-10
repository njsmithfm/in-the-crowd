<script>
  import shows from "../../../public/data/shows.json";

  const groupedByBorough = shows.reduce((acc, show) => {
    const borough = show.Borough;
    if (!acc[borough]) acc[borough] = [];
    acc[borough].push(show);
    return acc;
  }, {});
</script>
