import RunPipelineInline from '../../../components/RunPipelineInline';

async function getOpportunity(id: string) {
  const apiBase = process.env.API_BASE_URL || process.env.NEXT_PUBLIC_API_BASE_URL || '';
  try {
    const res = await fetch(`${apiBase}/opportunities/${id}`, { cache: 'no-store' });
    if (!res.ok) return null;
    const data = await res.json();
    return data;
  } catch (err) {
    return null;
  }
}

interface Params {
  params: { id: string };
}

export default async function OpportunityPage({ params }: Params) {
  const opportunity = await getOpportunity(params.id);
  if (!opportunity) {
    return <div>Opportunity not found</div>;
  }
  return (
    <div>
      <h1>{opportunity.name}</h1>
      <RunPipelineInline
        opportunityId={params.id}
        initialTaskId={opportunity.task_id || opportunity.taskId || null}
        webViewLink={opportunity.webViewLink || opportunity.complianceXlsxLink}
      />
      {opportunity.description && <p>{opportunity.description}</p>}
    </div>
  );
}
