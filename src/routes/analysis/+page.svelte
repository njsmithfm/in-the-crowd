<script>
  import shows from "../../../public/data/shows.json";

  const sortedShows = [...shows].sort((a, b) => b.Show_Number - a.Show_Number);

  let query = $state("");
  let selectedYear = $state("all");
  let selectedShow = $state(null);

  const years = [...new Set(sortedShows.map((show) => show.Year))].sort(
    (a, b) => b - a,
  );

  const filteredShows = $derived(
    sortedShows.filter((show) => {
      const matchesQuery =
        `${show.Artist} ${show.Venue} ${show.Borough} ${show.Notes ?? ""}`
          .toLowerCase()
          .includes(query.toLowerCase());

      const matchesYear =
        selectedYear === "all" || show.Year === Number(selectedYear);

      return matchesQuery && matchesYear;
    }),
  );

  const totalShows = $derived(sortedShows.length);
  const freeShows = $derived(
    sortedShows.filter((show) => show.Free_Show).length,
  );
  const showsWithNotes = $derived(
    sortedShows.filter((show) => show.Notes && show.Notes.trim()).length,
  );
</script>
