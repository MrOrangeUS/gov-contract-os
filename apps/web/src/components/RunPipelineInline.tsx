'use client';

import { useState, useEffect } from 'react';
import { runPipeline, getJobStatus } from '../lib/api';
import { useToast } from './ToastProvider';
import Link from 'next/link';

interface Props {
  opportunityId: string;
  initialTaskId?: string | null;
  webViewLink?: string | null;
}

export default function RunPipelineInline({
  opportunityId,
  initialTaskId = null,
  webViewLink: initialWebViewLink = null,
}: Props) {
  const [status, setStatus] = useState<'idle' | 'running' | 'completed' | 'failed'>('idle');
  const [webViewLink, setWebViewLink] = useState<string | null>(initialWebViewLink);
  const showToast = useToast();

  const handleClick = async () => {
    setStatus('running');
    try {
      const data = await runPipeline(opportunityId);
      const taskId =
        data.taskId ||
        data.task_id ||
        data.id ||
        data.jobId ||
        data.job_id;
      if (!taskId) {
        showToast('Failed to get task ID', 'error');
        setStatus('idle');
        return;
      }
      pollStatus(taskId);
    } catch (err) {
      showToast('Failed to start pipeline', 'error');
      setStatus('idle');
    }
  };

  const pollStatus = async (taskId: string) => {
    try {
      const data = await getJobStatus(taskId);
      if (data.state === 'PENDING' || data.state === 'STARTED') {
        setTimeout(() => pollStatus(taskId), 2000);
      } else if (data.state === 'SUCCESS') {
        setStatus('completed');
        setWebViewLink(data.webViewLink || data.complianceXlsxLink || null);
      } else {
        showToast('Pipeline failed', 'error');
        setStatus('failed');
      }
    } catch (err) {
      showToast('Failed to get status', 'error');
      setStatus('failed');
    }
  };

  useEffect(() => {
    if (initialTaskId) {
      pollStatus(initialTaskId);
    }
  }, [initialTaskId]);

  return (
    <>
      <Button disabled={status === 'running' || status === 'completed'} onClick={handleClick}>
        {status === 'running' ? 'Running...' : status === 'completed' ? 'Completed' : 'Run Pipeline'}
      </Button>
      {webViewLink && (
        <Link href={webViewLink} target="_blank" rel="noopener noreferrer">
          View Compliance XLSX
        </Link>
      )}
    </>
  );
}
