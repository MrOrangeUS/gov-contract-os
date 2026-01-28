import RunPipelineInline from '../../components/RunPipelineInline';
import Link from 'next/link';


async function getOpportunities() {
  const apiBase = process.env.API_BASE_URL || process.env.NEXT_PUBLIC_API_BASE_URL || '';
  try {
    const res = await fetch(`${apiBase}/opportunities`, { cache: 'no-store' });
    if (!res.ok) {
      return [];
    }
    const data = await res.json();
    return data.opportunities || data;
  } catch (err) {
    return [];
  }
}

export default async function OpportunitiesPage() {
  const opportunities = await getOpportunities();

  return (
<div>
  {opportunities.length === 0 ? (
    <div>
      <p>No opportunities found.</p>
      <Link href="/opportunities/new>Create Opportunity</Link>
    </div>
  ) : (
    <ul>
      {opportunities.map((opp: any) => (
        <li key={opp.id} style={{ marginBottom: '1rem' }}>
          <span>{opp.name}</span>
          {/* Inline Run Pipeline button */}
          <RunPipelineInline
            opportunityId={opp.id}
            initialTaskId={opp.task_id || opp.taskId || null}
            webViewLink={opp.webViewLink || opp.complianceXlsxLink}
          />
        </li>
      ))}
    </ul>
  )}
</div>
      
  );
}
