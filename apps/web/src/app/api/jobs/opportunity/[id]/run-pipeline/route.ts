import { NextResponse } from 'next/server';

// Proxy run pipeline request to the backend API
export async function POST(
  request: Request,
  { params }: { params: { id: string } }
) {
  const apiBase =
    process.env.API_BASE_URL || process.env.NEXT_PUBLIC_API_BASE_URL || '';
  try {
    const res = await fetch(
      `${apiBase}/jobs/opportunity/${params.id}/run-pipeline`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
    const data = await res.json();
    return new NextResponse(JSON.stringify(data), {
      status: res.status,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new NextResponse(
      JSON.stringify({ error: 'Failed to trigger pipeline' }),
      {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      }
    );
  }
}
