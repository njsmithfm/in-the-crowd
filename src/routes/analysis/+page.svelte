<script>
  import shows from "../../../public/data/shows.json";
  import AnalysisDashboard from "$lib/components/analysis/AnalysisDashboard.svelte";

  const sortedShows = [...shows].sort((a, b) => b.Show_Number - a.Show_Number);

  const boroughCounts = sortedShows.reduce((counts, show) => {
    counts[show.Borough] = (counts[show.Borough] ?? 0) + 1;
    return counts;
  }, {});

  const venueCounts = sortedShows.reduce((counts, show) => {
    counts[show.Venue] = (counts[show.Venue] ?? 0) + 1;
    return counts;
  }, {});

  const yearCounts = sortedShows.reduce((counts, show) => {
    counts[show.Year] = (counts[show.Year] ?? 0) + 1;
    return counts;
  }, {});

  const freeShowsByYear = sortedShows.reduce((counts, show) => {
    if (show.Free_Show) {
      counts[show.Year] = (counts[show.Year] ?? 0) + 1;
    }

    return counts;
  }, {});

  const boroughData = Object.entries(boroughCounts)
    .map(([label, value]) => ({ label, value }))
    .sort((a, b) => b.value - a.value);

  const venueData = Object.entries(venueCounts)
    .map(([label, value]) => ({ label, value }))
    .sort((a, b) => b.value - a.value)
    .slice(0, 5);

  const timelineData = Object.entries(yearCounts)
    .map(([label, value]) => ({ label, value }))
    .sort((a, b) => Number(a.label) - Number(b.label));

  const freeShowData = Object.entries(freeShowsByYear)
    .map(([label, value]) => ({ label, value }))
    .sort((a, b) => Number(a.label) - Number(b.label));

  const totalShows = sortedShows.length;
  const freeShows = sortedShows.filter((show) => show.Free_Show).length;
  const showsWithNotes = sortedShows.filter(
    (show) => show.Notes && show.Notes.trim(),
  ).length;

  const yearsCovered = new Set(sortedShows.map((show) => show.Year)).size;
  const topBorough = boroughData[0]?.label ?? "N/A";
  const topVenue = venueData[0]?.label ?? "N/A";
</script>

<svelte:head>
  <title>Analysis</title>
</svelte:head>

<AnalysisDashboard
  stats={{
    totalShows,
    freeShows,
    showsWithNotes,
    yearsCovered,
    topBorough,
    topVenue,
  }}
  {boroughData}
  {venueData}
  {freeShowData}
  {timelineData}
/>
